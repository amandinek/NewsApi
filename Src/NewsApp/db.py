import psycopg2
import sys

con=None
con=psycopg2.connect(database='wuxsedzk',
                         user='wuxsedzk',
                         password='HMMcvpu7-6UvZE-fpTHSQcQ4Td0K2jKz',
                         host='balarama.db.elephantsql.com',
                         port='5432')
with con:
    cur=con.cursor()

    cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
    print("data inserted")
    con.commit()
