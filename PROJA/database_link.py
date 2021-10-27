
import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='password',
    port=5432
)

cur = con.cursor()

# cur.execute("select atribuut, atribuut from tabel")

# cur.execute('insert into tabel (attribuut, attribuut, attribuut) values (%s, %s, %s)',
#                (attribuut, attribuut, attribuut))

rows = cur.fetchall()

for r in rows:
    print(f"atribuut {r[0]} atribuut {r[1]}")

cur.close()

con.close()
