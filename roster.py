import sys
import sqlite3
from sqlite3 import Error

#print(sys.argv[1])
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn, house):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE house=? ORDER BY last ASC, first ASC;", (house,))

    rows = cur.fetchall()

    for row in rows:
        if row[2] == None:
            print(row[1],' ', row[3],", born ", row[5], sep='')
        else:
            print(row[1],' ', row[2],' ', row[3],", born", ' ', row[5], sep='')


def main():
    database = r"students.db"

    # create a database connection
    conn = create_connection(database)
    with conn:



        select_all_tasks(conn, (sys.argv[1]))


if __name__ == '__main__':
    main()