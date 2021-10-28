
import psycopg


def collectItems():
    sql = "SELECT * from collection"
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

    for item in rows:
        print(item[1])


con = psycopg.connect(
    host='localhost',
    dbname='twitter',
    user='postgres',
    password='admin',
    port=4444
)

collectItems()
