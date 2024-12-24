import sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table, and_

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()