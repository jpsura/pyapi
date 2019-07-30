#!/usr/bin/env python3 

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Database correctly")

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
        (ID INT PRIAMRY KEY NOT NULL,
        NAME TEXT NOT NULL, 
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);''')
print("table created successfully")
conn.close()
