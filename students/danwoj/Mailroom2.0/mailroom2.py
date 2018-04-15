#!/usr/bin/python

import sqlite3 as lite
import sys

db_con = None
db_file = 'don_list.db'

#try:
#    db_con = lite.connect(db_file)

#    cur = db_con.cursor()    
#    cur.execute('.schema don_list')

def cmd_db(sql_state):
    db_con = lite.connect(db_file)
    cur = db_con.cursor()
    cur.execute(sql_state)
    data = cur.fetchone()
    return data

#    data = cur.fetchone()

#    print(data)

#except lite.Error(e):

#    print("Error %s:" % e.args[0])
#    sys.exit(1)

#finally:

#    if db_con:
#        db_con.close()