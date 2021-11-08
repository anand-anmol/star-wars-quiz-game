from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime

class Score(Base):
    """ Score """

    __tablename__ = "score"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    score = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, name, score):
        """ Initializes a application record """
        self.name = name
        self.score = score
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        """ Dictionary Representation of an application """
        dict = {}
        dict['name'] = self.name
        dict['score'] = self.score
        dict['date_created'] = self.date_created

        return dict