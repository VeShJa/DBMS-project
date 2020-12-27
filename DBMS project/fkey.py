import sqlite3

conn = sqlite3.connect('dAtAbase.sqlite')
cur=conn.cursor()



ar=list()
cur.execute('SELECT * FROM Officer ORDER BY sector_no')
cur.execute('SELECT id FROM Officer')
idd=cur.fetchall()
for num in idd:
    ar.append(num[0])
print(ar)
k=1
for sec in range(1,46):
    cur.execute("""
            UPDATE Customer SET officer_id= (?)
            WHERE sector_no = (?)
            """,(k, sec))
    k=k+1
