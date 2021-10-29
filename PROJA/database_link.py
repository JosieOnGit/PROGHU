
import psycopg


def collectItems():
    sql = "SELECT * from TwitterDB"
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

    messageID = 0
    for item in rows:
        print(item[0])
        messageID += 1
    print(messageID)


con = psycopg.connect(
    host='localhost',
    dbname='Twitter',
    user='postgres',
    password='admin',
    port=4444
)

collectItems()
