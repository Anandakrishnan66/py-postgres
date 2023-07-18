import psycopg2

conn= psycopg2.connect(host="localhost",port="5432",dbname="postgres", user="api",password="537591")

cur=conn.cursor()


cur.execute("SELECT * FROM users")

records = cur.fetchall()

print(records)
