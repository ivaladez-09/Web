"""Create a SQLite database and add information to it."""
import sqlite3

if __name__ == "__main__":
    # Basic objects for SQLite database manipulation
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()

    # Create our SQL query and execute it
    query = "CREATE TABLE IF NOT EXISTS items (" \
            "name TEXT PRIMARY KEY," \
            "price INTEGER);"
    cursor.execute(query)

    # Insert some users
    query = "INSERT INTO items (name, price) VALUES(?, ?);"
    rows = [("Chair", 12.5),
            ("Table", 28.9),
            ("TV", 35.2)]
    for row in rows:
        cursor.execute(query, row)

    # Save changes and close the connection to the database
    connection.commit()
    connection.close()
