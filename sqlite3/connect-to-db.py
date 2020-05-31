import sqlite3


def main():
    try:
        DB = sqlite3.connect("users.db")
        print("the database is connected successfully")
        DB.close()
    except sqlite3.DatabaseError:
        print("can't connect to db")


if __name__ == '__main__':
    main()
