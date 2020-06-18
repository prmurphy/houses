import csv
import sys
import sqlite3
from sqlite3 import Error

#code take from https://realpython.com/python-csv/
#with open("characters.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        else:
#            print(f'\t{row[0]} is house {row[1]}, and was born in {row[2]}.')
#            line_count += 1
#    print(f'Processed {line_count} lines.')

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

def insert_name(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO students (first,middle,last,house,birth)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():

    database = r"students.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #task_1 = ("test", "test", "test", "test", "test")
        #insert_name(conn, task_1)
        #print("test insert")

        #code take from https://realpython.com/python-csv/
        with open(sys.argv[1]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    #print(f'\t{row[0]} is house {row[1]}, and was born in {row[2]}.')
                    #find how many names the person has
                    x = row[0].split()
                    if len(x) == 2:
                        #print("2 names")
                        task_1 = (x[0], None, x[1], row[1], row[2])
                        insert_name(conn, task_1)
                    if len(x) == 3:
                        #print("3 names", x[0])

                        task_1 = (x[0], x[1], x[2], row[1], row[2])
                        insert_name(conn, task_1)
                    line_count += 1
            #print(f'Processed {line_count} lines.')

if __name__ == '__main__':
    main()