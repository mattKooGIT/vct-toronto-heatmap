import psycopg2

conn = psycopg2.connect(
    dbname = "valorant",
    user = "postgres",
    host = "localhost"
)

cur = conn.cursor()

cur.execute("SELECT version();")
version = cur.fetchone()
print("PostgreSQL version:", version)

cur.close()
conn.close()