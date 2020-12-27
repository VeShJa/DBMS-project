import sqlite3
conn = sqlite3.connect('dAtAbase.sqlite')
cur=conn.cursor()

cur.executescript('''

PRAGMA foreign_keys = 0;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Officer;
DROP TABLE IF EXISTS Bills;
DROP TABLE IF EXISTS Reservoir;
DROP TABLE IF EXISTS Locality;
PRAGMA foreign_keys = 1;
''')
cur.execute('''
CREATE TABLE officer(
    "id" INTEGER PRIMARY KEY NOT NULL UNIQUE ,
    "Name" TEXT NOT NULL,
    "sector_no" INTEGER
)
''')
cur.execute('''
CREATE TABLE Reservoir(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "Name" TEXT UNIQUE,
    "Water_level" INTEGER
);
''')
cur.execute('''
CREATE TABLE Locality(
    "sector_no" INTEGER PRIMARY KEY NOT NULL UNIQUE,
    "Area_Name" TEXT,
    "Water_Supply_Date" INTEGER,
    "officer_id" INTEGER,
    "reservoir_id" INTEGER NOT NULL,
    FOREIGN KEY("officer_id") REFERENCES "Officer"("id"),
    FOREIGN KEY("reservoir_id") REFERENCES "Reservoir"("id")
);
''')
cur.execute('''
CREATE TABLE Bills(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "Payments_Due" INTEGER NOT NULL,
    "due_Date" INTEGER,
    "customer_id" INTEGER,
    FOREIGN KEY("customer_id") REFERENCES "Customer"("id")
);
''')
cur.execute('''
CREATE TABLE Customer(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "Name" TEXT,
    "Address" TEXT,
    "sector_no" NOT NULL,
    "officer_id" INTEGER NOT NULL,
    "reservoir_id" INTEGER NOT NULL,
    "bill_id" INTEGER NOT NULL,
    "no_of_connection" INTEGER DEFAULT "1",
    FOREIGN KEY("sector_no") REFERENCES "Locality"("sector_no"),
    FOREIGN KEY("officer_id") REFERENCES "Officer"("id"),
    FOREIGN KEY("reservoir_id") REFERENCES "Reservoir"("id"),
    FOREIGN KEY("bill_id") REFERENCES "Bills"("id")
);
''')
conn.commit()
cur.close()
