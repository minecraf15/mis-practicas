import sqlite3

conexion=sqlite3.connect('gaku.db')

cursor=conexion.cursor()




menu=[('12345','ELIEZER',12),('09245','CAB',13),('23455',"lobo",15),]
 
cursor.executemany(" INSERT INTO gaku VALUES(?,?,?)",menu)

cursor.execute("SELECT * FROM gaku")
x=cursor.fetchall()
for i in x:
    print(i)
   
conexion.commit()
conexion.close()