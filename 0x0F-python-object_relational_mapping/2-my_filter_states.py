#!/usr/bin/python3
"""
Lists states securely against SQL injection.
+"""
import MySQLdb
from sys import argv


if len(argv) < 4:
    print("Usage: {} <username> <password> <database>".format(argv[0]))
    exit(1)

try:
    db_connection = MySQLdb.connect(
     host="localhost",
     port=3306, user=argv[1],
     passwd=argv[2],
     db=argv[3],
     charset="utf8"
    )

    cursor = db_connection.cursor()

    cursor.execute(
        f"SELECT * FROM states WHERE BINARY name = '{argv[4]}' ORDER BY id ASC;")
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db_connection.close()

except MySQLdb.Error as e:
    print("Error connecting to the database:", e)
