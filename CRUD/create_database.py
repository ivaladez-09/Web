"""Create a SQLite database and add information to it."""
import sqlite3

if __name__ == "__main__":
    # Basic objects for SQLite database manipulation
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()

    # Create our SQL query and execute it
    query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT," \
            "username text," \
            "password text," \
            "age INTEGER);"
    cursor.execute(query)

    # Insert some users
    query = "INSERT INTO users (username, password, age) VALUES(?, ?, ?)"
    rows = [('Ivan', 'asdf', 24),
            ('Susana', 'zxcv', 22),
            ('Aaron', 'qwer', 20)]
    for row in rows:
        cursor.execute(query, row)

    # Save changes and close the connection to the database
    connection.commit()
    connection.close()
