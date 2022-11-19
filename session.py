from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:witek_22@localhost:3306/articleshashtags")
session = sessionmaker(bind=engine)

