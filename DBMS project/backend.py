import sqlite3

def addCustomer(Name, sector_no, Address, Number_of_Connections, officer_id, bill_id,Reservoir_id):
    conn = sqlite.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    Name = str(Name)
    sector_no = int(sector_no)
    Number_of_Connections = int (Number_of_Connections)
    officer_id = int(officer_id)
    bill_id = int(bill_id)
    Reservoir_id = int(Reservoir_id)
    cur.execute('''INSERT INTO Customer(Name, address, sector_no, no_of_connection, bill_id, officer_id, reservoir_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''(Name, Address, sector_no, Number_of_Connections, bill_id, officer_id, Reservoir_id))
    cur.close()
    conn.commit()

def addOfficer(id, Name, sector_no):
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    ido = int(id)
    Nameo = str(Name)
    sector_noo = int(sector_no)
    cur.execute("INSERT INTO Officer(id, Name, sector_no) VALUES (?,?,?)"(ido, Nameo, sector_noo))
    cur.close()
    conn.commit()

def addReservoir(Name, Water_level):
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO Reservoir(Name, Water_level) VALUES (?,?)"(Name, Water_level))
    cur.close()
    conn.commit()

def addLocality(sector_no, Area, waterDate, officer, reservoir):
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Locality (sector_no, Area_Name, Water_Supply_Date, officer_id, reservoir_id)
        VALUES(?, ?, ?, ?, ?)'''(sector_no, Area, waterDate, officer, reservoir))
    cur.close()
    conn.commit()

def delCustomer(id):
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    inputID = int(id)
    cur.execute("DELETE from Customer WHERE id = ? "(inputID,))
    conn.commit()
    cur.close()

def delOfficer(id):
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    ido = int(id)
    cur.execute("DELETE from Officer WHERE id = ? ",(ido,))
    conn.commit()
    cur.close()

def deleteReservoir(id):
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    inputID = int(id)
    cur.execute("DELETE from Reservoir WHERE id = ? ",(inputID,))
    conn.commit()
    cur.close()

def viewCustomer():
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Customer")
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    return rows

def viewOfficer():
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Officer")
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    return rows

def viewReservoir():
    conn = sqlite3.connect('dAtAbase.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Reservoir")
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    return rows

def viewBillsOfCustomer(Bill_id):
    conn = sqlite3.connect('dAtAbase,sqlite')
    cur = conn.cursor()
    cur.execute("SELECT Payments_Due FROM Bills,Customer WHERE Bill.id = (?)"(Bill_id))
    amount = cur.fetchall()
    return amount
