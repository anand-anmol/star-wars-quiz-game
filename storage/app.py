import connexion, yaml, logging.config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from score import Score

# Set up external config file
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

# Set up logging
with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basicLogger')

logger.info(f'Connecting to DB. Hostname:{app_config["datastore"]["hostname"]}, Port:{app_config["datastore"]["port"]}')

DB_ENGINE = create_engine(f'mysql+pymysql://{app_config["datastore"]["user"]}:{app_config["datastore"]["password"]}@{app_config["datastore"]["hostname"]}:{app_config["datastore"]["port"]}/{app_config["datastore"]["db"]}')
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def store_score(body: dict):
    """ Responds to post requests at /score and stores them in a database """
    
    try:

        score = Score(name=body['name'], score=body['score'])

        session = DB_SESSION()

        session.add(score)

        session.commit()
        session.close()

        logger.info(f"Score saved {body['name']} - {body['score']}")

        return 'Score saved successfully', 201
    
    except Exception as e:

        logger.error(e)

        return 'invalid input, object invalid', 400

def get_top_scores():
    """ Returns top 10 scores from database for the leaderboard """

    try:

        session = DB_SESSION()

        scores= session.query(Score).order_by(Score.score.desc(), Score.date_created.desc()).limit(10)

        session.close()

        scores = [score.to_dict() for score in scores]
    
    except Exception as e:

        logger.error(e)

        return 'Trouble getting top scores', 500

    return scores, 200


# Set up config for FlaskApp
app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
   
    app.run(port=8090)