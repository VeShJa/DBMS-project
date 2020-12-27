import sqlite3
#BACKEND

def officerData():
    con = sqlite3.connect("dAtAbase.sqlite")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS officer (id INTEGER PRIMARY KEY, Name text, sector_no text)")
    con.commit()
    con.close()

def addOfficer(id, Name, sector_no):
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("INSERT INTO officer VALUES (?, ?, ?)", (id, Name, sector_no))
    con.commit()
    con.close()

def viewOfficer():
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM officer")
    rows = cur.fetchall()
    con.close()
    return rows

def delOfficer(id):
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("DELETE FROM officer WHERE id=?",(id))
    con.commit()
    con.close()

def reservoirData():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Reservoir (id INTEGER PRIMARY KEY, Name text, Water_level text)")
    con.commit()
    con.close()

def addReservoir():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Reservoir VALUES (?, ?, ?)", (id, Name, Water_level))
    con.commit()
    con.close()

def delReservoir():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("DELETE FROM Reservoir WHERE id=?",(id))
    con.commit()
    con.close()

def viewReservoir():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM officer")
    rows = cur.fetchall()
    con.close()
    return rows

def billData():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Bills ('id' INTEGER PRIMARY KEY,  'Payments_Due' INTEGER, 'due_Date' INTEGER, 'customer_id' INTEGER, FOREIGN KEY('customer_id') REFERENCES 'Customer'('id'))")
    con.commit()
    con.close()

def addBill():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Bills VALUES (?, ?, ?)", (id, Name, Water_level))
    con.commit()
    con.close()

def delBill():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("DELETE FROM Bills WHERE id=?",(id))
    con.commit()
    con.close()

def viewBill():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Bills")
    rows = cur.fetchall()
    con.close()
    return rows

officerData()
reservoirData()
billData()
