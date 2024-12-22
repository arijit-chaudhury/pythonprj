import pandas as pd
from sqlalchemy import create_engine

query = ''' SELECT * FROM assetdistribution; '''
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()
df = pd.read_sql(query, conn)
print(df.head())