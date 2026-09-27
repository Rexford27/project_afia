#the goal of this is to set up configuration to my database 
#it set up connection back needs to talk to supabase and the session toold 
#session currect working 
#the enfgine is the publing 

import os


from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

#establish connection to database so SQLAlchemy knows how to comunicate with database
engine = create_engine(DATABASE_URL)

#session maker
SessionLocal = sessionmaker(bind=engine)

def get_db():
    #instace of session
    db = SessionLocal()

    try:
        #hand off the db 
        yield db
    #always gets it back
    finally:
        db.close() 
#engine the phone company
#db instnace is a phone call
#yield handing off the pone\
#getting the phone and hanguing up despite what ever happen 