import sqlite3


def main():
    try:
        DB = sqlite3.connect("users.db")
        t_query = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY" + \
                  "KEY, name TEXT, password TEXT)"
        insert = "INSERT INTO users(id, name, password) VALUES(?, ?, ?)"
        DB.execute(t_query)
        DB.execute("insert into users(id, name, password) values(?,?,?)", (1, 'user1', 'password1'))
        DB.commit()
        print("data is added successfully")
        DB.close()
    except sqlite3.DatabaseError as e:
        print(e)


if __name__ == '__main__':
    main()
