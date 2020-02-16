from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# sqllite engine
engine = create_engine('sqlite:///chartbuster.db')
Session = sessionmaker(bind=engine)

# kaggle data source
dataSource = "data/top10s.csv"
