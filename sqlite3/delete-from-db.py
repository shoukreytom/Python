import sqlite3


DB = sqlite3.connect('users.db')
DB.row_factory = sqlite3.Row


def list_users():
    statement = "SELECT * FROM users"
    cursor = DB.execute(statement)
    counter = 0
    for row in cursor:
        counter += 1
        print(f"{row['id']}\t{row['name']}\t{row['password']}")
    return counter


def delete(user_id):
    statement = f"DELETE FROM users WHERE id = {user_id}"
    DB.execute(statement)
    DB.commit()


def main():
    print("users in db before deletion")
    total = list_users()
    print(f"Total: {total} users")
    delete(1)
    print("users in db after deletion")
    total = list_users()
    print(f"Total: {total} users")


if __name__ == '__main__':
    main()
