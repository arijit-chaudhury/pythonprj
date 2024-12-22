import sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table, and_

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()
metadata = sqlalchemy.MetaData()
assetdistribution = sqlalchemy.Table('assetdistribution', metadata, autoload_with=engine)

print(assetdistribution.columns.keys())
query = sqlalchemy.select([assetdistribution])
resultProxy = conn.execute(query)
result = resultProxy.fetchall()
for r in result:
    print(r)