from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///chartbuster.db')
Session = sessionmaker(bind=engine)
