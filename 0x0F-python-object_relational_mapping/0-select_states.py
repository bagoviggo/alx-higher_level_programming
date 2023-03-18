#!/usr/bin/env python3
"""A script that selects all states from hbtn_0e_0 database"""
import sys
import MySQLdb


if __name__ == '__main__':
    # Check the number of arguments
    try:
        # Connect to the database
        connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        # Get a cursor
        cursor = connection.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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
        connection.close()
