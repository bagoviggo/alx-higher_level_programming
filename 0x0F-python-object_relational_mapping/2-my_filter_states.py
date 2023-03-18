#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 5:
    print("Usage: {} username password database_name state_name".format(sys.argv[0]))
    exit(1)

# Get command line arguments
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

# Create cursor object
cursor = db.cursor()

# Execute SQL query
sql_query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
cursor.execute(sql_query, ('%' + state_name + '%',))

# Print results
results = cursor.fetchall()
for row in results:
    print(row)

# Close database connection
db.close()
