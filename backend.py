import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , temperature float , Pulse text , Respiration text , BP text ,Weight float)")
    conn.commit()
    conn.close()

def insert(date , temperature , Pulse , Respiration , BP , Weight):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , temperature , Pulse , Respiration , BP , Weight))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , temperature='' , Pulse='' , Respiration='' , BP='' , Weight=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR temperature=? OR Pulse=? OR Respiration=? OR BP=? OR Weight=?" , (date , temperature , Pulse , Respiration , BP , Weight))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
