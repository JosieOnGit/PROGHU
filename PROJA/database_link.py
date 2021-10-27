
import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='password',
    port=5432
)

cur = con.cursor()

cur.execute("select attribuut, attribuut from tabel")

cur.execute('insert into tabel (attribuut, attribuut, attribuut) values (%s, %s, %s)',
           (attribuut, attribuut, attribuut))

rows = cur.fetchall()

for r in rows:
    print(f"attribuut {r[0]} attribuut {r[1]}")

cur.close()

con.close()
