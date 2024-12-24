import psycopg2

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", port="5432", host="localhost")
except:
    print("I am unable to connect to the database")

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
except:
    print("I can't drop our test database!")

conn.commit()
conn.close()
cursor.close()