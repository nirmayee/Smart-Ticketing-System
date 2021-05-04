import sqlite3
import serial
conn = sqlite3.connect('C://Users//Nirmayee//Downloads//project database.db')
cp = conn.cursor()


l=('1234',)
k=cp.execute("SELECT * FROM cool WHERE ID=?",l)
print(cp.fetchall())
