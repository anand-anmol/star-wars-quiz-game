import requests, yaml, json, connexion, logging.config, random, os
from flask_cors import CORS
from threading import Thread
from filelock import FileLock

# Set up external config file
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

# Set up logging
with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basicLogger')

HEADERS = {"content-type":"application/json"}

def get_questions():
    """ 
    Responds to get requests at /questions and returns first set of questions
    from json file
    """

    if os.path.isfile(app_config['questionstore']['filename']):

        # Read file, return first set of questions and remove them from file
        with FileLock(f"{app_config['questionstore']['filename']}.lock"):

            with open(app_config['questionstore']['filename'], 'r') as file:
                questions = json.load(file)

            try:
                ques_to_return = questions.pop(0)
            except IndexError:
                return "Questions are still being made", 400

            with open(app_config['questionstore']['filename'], 'w') as file:
                json.dump(questions, file)
        
        # Start up a new thread to create questions if running low
        if len(questions) < 25:

            t1 = Thread(target=populate_questions)
            t1.setDaemon(True)
            logger.info(f'Starting Thread {t1} to create more questions')
            t1.start()

        return ques_to_return, 200

    else:

        return "Questions are still being made", 400

def populate_questions():
    """ Writes questions to file """

    # Read questions from file and create it if it doesn't exist
    if os.path.isfile(app_config['questionstore']['filename']):
        with open(app_config['questionstore']['filename'], 'r') as file:
            questions = json.load(file)
    else:
        questions = []
        with FileLock(f"{app_config['questionstore']['filename']}.lock"):
            with open(app_config['questionstore']['filename'], 'w') as file:
                json.dump(questions, file)

    while len(questions) < app_config['questionstore']['num_questions']:

        # create questions for every entity
        temp_questions = []

        for entity in app_config['entities']:
            
            temp_questions += create_questions(entity)

        # Write newly created functions to file
        with FileLock(f"{app_config['questionstore']['filename']}.lock"):

            with open(app_config['questionstore']['filename'], 'r') as file:
                questions = json.load(file)

            if len(temp_questions) >= 5:
                questions.append(random.sample(temp_questions, 5))

            with open(app_config['questionstore']['filename'], 'w') as file:

                logger.info(f'Writing {len(questions)} set(s) of questions to file')
                json.dump(questions, file)
    
    logger.info('Thread exited after storing questions in file')

def create_questions(entity: str):
    """ Creates question for entity based on template file using API data """

    # Get entity data from API
    response = requests.get(f"{app_config['baseurl']}{entity}")

    if response.status_code == 200:
        entity_data_all = response.json()['results']
    else:
        logger.debug(f'Failed to retrieve data from API. Error: {response.content}')
        return []

    # Read question template for entity
    with open(f"{app_config['templatestore']['dirname']}{entity}.json", 'r') as file:
        questions = json.load(file)
    
    # Substitute data for questions in template
    for index, ques in enumerate(questions):

        entity_data_singular = entity_data_all.pop(random.randint(0, len(entity_data_all) - 1))
        for property in ques["properties_to_replace"]:
            ques["question"] = ques["question"].replace(f"#({property})", str(entity_data_singular[property]))
        
        answer_property = ques["correct_answer"]
        ques["correct_answer"] = entity_data_singular[answer_property]
        ques["options"] = {ques["correct_answer"]}
        ques["options"].update([answer[answer_property] for answer in random.sample(entity_data_all, 3)])

        while len(ques["options"]) < 4:
            ques["options"].add(random.choice(entity_data_all)[answer_property])

        ques["options"] = list(ques["options"])

        del ques["properties_to_replace"]
        
        questions[index] = ques
    
    return questions

def store_score(body: dict):
    """ Responds to post requests at /score and forwards them to the storage service """
    
    response = requests.post(app_config['scorestore']['url'], data=json.dumps(body), headers=HEADERS)

    print(response.text)

    if response.status_code == 201:
        return 'Score saved successfully', 201
    else:
        return 'invalid input, object invalid', 400

# Set up config for FlaskApp
app = connexion.FlaskApp(__name__, specification_dir='')

app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)

CORS(app.app)
app.app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":

    t1 = Thread(target=populate_questions)
    t1.setDaemon(True)
    t1.start()

    app.run(port=8080)