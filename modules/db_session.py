import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

DB_URL='postgresql://admin:admin@localhost:5432/pruebas'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
