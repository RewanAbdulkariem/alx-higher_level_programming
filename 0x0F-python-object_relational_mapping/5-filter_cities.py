#!/usr/bin/python3
"""
Lists cities of a specific state.
"""
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
        "SELECT cities.id, cities.name, states.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             ORDER BY id ASC;")
    query_rows = cursor.fetchall()

    city_names = [row[1] for row in query_rows if argv[4] in row]
    print(", ".join(city_names))

    cursor.close()
    db_connection.close()

except MySQLdb.Error as e:
    print("Error connecting to the database:", e)
