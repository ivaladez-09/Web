"""Model - Interface for data in the Database"""
import sqlite3

DATABASE = "items.db"


class Items:
    """"""
    def __init__(self, item, price):
        """"""
        self.item = item
        self.price = price

    @classmethod
    def post(cls, item, price):
        """"""
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        try:
            query = "INSERT INTO items (name, price) VALUES(?, ?)"
            parameters = (str(item), float(price))  # It has to be a Tuple
            cursor.execute(query, parameters)
            user = cls(*parameters)

        except Exception as err:
            print("Error: {}".format(err))
            user = None

        connection.commit()
        connection.close()

        return user

    @classmethod
    def get(cls, item):
        """"""
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        try:
            query = "SELECT * FROM items WHERE name=? LIMIT 1"
            parameters = (str(item), )  # It has to be a Tuple
            row = cursor.execute(query, parameters)
            row = row.fetchone()  # ("Chair": 15.5)
            user = cls(*row)

        except Exception as err:
            print("Error: {}".format(err))
            user = None

        connection.commit()
        connection.close()

        return user
