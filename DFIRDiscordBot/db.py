from DFIRDiscordBot.models import Base
import sqlalchemy

class DB():

    def __init__(self):
        self.engine = sqlalchemy.create_engine("sqlite:///db.sqlite", echo=True, future=True)
        Base.metadata.create_all(self.engine)

db = DB()
