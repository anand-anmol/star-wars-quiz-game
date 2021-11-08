from io import open_code
import requests, yaml, json, connexion, logging.config, random
from connexion import NoContent
from flask_cors import CORS, cross_origin

ENTITIES = ['people', 'planets', 'films', 'species', 'vehicles', 'starships']

BASE_URL = 'https://swapi.dev/api'

# with open('app_conf.yml', 'r') as f:
#     app_config = yaml.safe_load(f.read())

# with open('log_conf.yml', 'r') as f:
#     log_config = yaml.safe_load(f.read())
#     logging.config.dictConfig(log_config)

# logger = logging.getLogger('basicLogger')

def get_questions():

    questions = []

    for entity in ENTITIES:
        questions += create_questions(entity)
    
    print(questions)

    return random.sample(questions, 5), 200

def create_questions(entity):

    response = requests.get(f'{BASE_URL}/{entity}')

    entity_data_all = response.json()['results']

    with open(f'question_templates/{entity}.json', 'r') as file:
        questions = json.load(file)
    
    for index, ques in enumerate(questions):

        entity_data_singular = entity_data_all.pop(random.randint(0, len(entity_data_all) - 1))
        for property in ques["properties_to_replace"]:
            ques["question"] = ques["question"].replace(f"#({property})", str(entity_data_singular[property]))
        
        answer_property = ques["correct_answer"]
        ques["correct_answer"] = entity_data_singular[answer_property]
        ques["incorrect_answers"] = [answer[answer_property] for answer in random.sample(entity_data_all, 3)]
        
        del ques["properties_to_replace"]
        
        questions[index] = ques
    
    return questions


app = connexion.FlaskApp(__name__, specification_dir='')

app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)

CORS(app.app)
app.app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    app.run(port=8080)