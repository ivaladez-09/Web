import sqlite3


class User:
    """Class to handle the access to the database and create objects according the content"""

    def __init__(self, _id, username, password, age):
        """
        Initialize user class and store the required information for the database.
        :param _id: Integer user identifier
        :param username: String with the name to use by the user
        :param password: String with the password to access his/her data
        :param age: Integer with the current age of the user
        """
        self.id = _id
        self.username = username
        self.password = password
        self.age = age

    @classmethod
    def get_user(cls, username):
        """
        Getting the given user from the database.
        :param username: String with the username to search
        :return rows_list: List with User objects with the information from the database.
        """
        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()
        rows_list = list()

        try:
            query = 'SELECT * FROM users where username=?'
            rows = cursor.execute(query, (username,))  # Passing arguments to the query
            for row in rows:
                print(row)
                rows_list.append(cls(*row))

        except Exception as err:
            print(err)

        connection.commit()
        connection.close()

        return rows_list

    @classmethod
    def post_user(cls, username, password, age):
        """
        Adding the given user to the database.
        :param username: String with the username to search
        :param password: String with the user password
        :param age: Integer with the user age

        :return user: User object with the information added to the database.
        """
        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()

        try:
            query = 'INSERT INTO users (username, password, age) VALUES(?, ?, ?)'
            parameters = (username, password, age)
            cursor.execute(query, parameters)
            user = cls(None, *parameters)

        except Exception as err:
            print(err)
            user = None

        connection.commit()
        connection.close()

        return user

    @classmethod
    def put_user(cls, username, password=None, age=None):
        """
        Adding or updating the given user to the database.
        :param username: String with the username to search
        :param password: String with the user password
        :param age: Integer with the user age

        :return user: User object with the information added to the database.
        """
        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()
        users = User.get_user(username)
        if users:
            # print(users)
            for user in users:
                try:
                    if user.password == password and user.age != age:  # Update
                        query = "UPDATE users SET age=? WHERE username=? AND password=?"
                        parameters = (age, username, password)
                        cursor.execute(query, parameters)
                        new_user = cls(user.id, user.username, user.password, age)
                        break

                    elif user.age == age and user.password != password:  # Update
                        query = "UPDATE users SET password=? WHERE username=? AND age=?"
                        parameters = (password, username, age)
                        cursor.execute(query, parameters)
                        new_user = cls(user.id, user.username, password, user.age)
                        break

                except Exception as err:
                    print(err)
                    new_user = None
        else:  # Insert
            try:
                query = 'INSERT INTO users (username, password, age) VALUES(?, ?, ?)'
                parameters = (username, password, age)
                cursor.execute(query, parameters)
                new_user = cls(None, *parameters)

            except Exception as err:
                print(err)
                new_user = None

        connection.commit()
        connection.close()

        return new_user

    @classmethod
    def delete_user(cls, username, password, age):
        """
        Deleting the given user to the database.
        :param username: String with the username to search
        :param password: String with the user password
        :param age: Integer with the user age

        :return user: User object with the information added to the database.
        """
        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()

        try:
            query = 'DELETE FROM users WHERE username=? AND password=? AND age=?'
            parameters = (username, password, age)
            cursor.execute(query, parameters)
            user = cls(None, *parameters)

        except Exception as err:
            print(err)
            user = None

        connection.commit()
        connection.close()

        return user
