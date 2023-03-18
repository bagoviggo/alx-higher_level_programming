#!/usr/bin/env python3
import sys
import MySQLdb


if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the database
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Get a cursor
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        sys.exit(1)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
