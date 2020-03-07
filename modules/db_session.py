import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from .constants import Constants as cts 

cts = cts()
engine = create_engine(cts.DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
