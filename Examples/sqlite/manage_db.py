import random
import sqlite3
# from sqlite3 import Error  # It's not needed if you use sqlite3.Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error:
        print(sqlite3.Error)

    return conn


def create_table(conn):

    create_query = """CREATE TABLE IF NOT EXISTS cards (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        number VARCHAR(16) UNIQUE,
                        pin VARCHAR(4),
                        balance INTEGER DEFAULT 0
                      );"""

    cur = conn.cursor()
    cur.execute(create_query)


def gen_unique_card_number(conn):

    cur = conn.cursor()
    cur.execute("SELECT number FROM cards;")
    all_num_list = list(cur.fetchall())

    num = random.randrange(0, 10000)
    if num not in all_num_list:
        return num
    else:
        gen_unique_card_number(conn)


def insertion_test(conn):

    card_number = gen_unique_card_number(conn)
    # The proper way to do SQL queries is letting the sqlite3 library
    # formatting the strings, so you must follow the docs
    # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute
    insert_query = """INSERT INTO cards (
                        number,
                        pin,
                        balance
                     )
                     VALUES (
                        :card_number,
                        1234,
                        150
                     );"""

    cur = conn.cursor()
    cur.execute(insert_query, {"card_number": card_number})
    conn.commit()


conn = create_connection("card.s3db")

if conn is not None:
    create_table(conn)
    insertion_test(conn)
else:
    print("Error! Cannot create the database connection.")
