import sqlite3


DB = sqlite3.connect("users.db")


def main():
    try:
        DB.row_factory = sqlite3.Row
        select = "SELECT * FROM users"
        result = DB.execute(select)
        for row in result:
            print(f"id: {row['id']}\tname: {row['name']}\tpassword: {row['password']}")
        DB.close()
    except sqlite3.DatabaseError as e:
        print(e)


if __name__ == '__main__':
    main()
