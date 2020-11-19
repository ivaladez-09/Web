"""
Main file for CRUD System

NOTES:
    - html files need to be inside a folder called 'templates'
    - css files need to be inside a folder called 'static'.
      Also, remember to clean up the cache from the browser every time you make a change
      in the css file.
"""
import os
from flask import Flask, render_template, request, url_for, redirect
from user import User

app = Flask(__name__)

# Root CRUD interface
@app.route('/')
def home_page():
    return render_template('index.html')


# CRUD interfaces (POST, GET, PUT, DELETE). Example: /get.html
@app.route('/<string:method>.html')
def method_page(method='index.html'):
    return render_template('{}.html'.format(method), method=method)


# HTTP methods
@app.route('/get.html/submit', methods=['GET'])
def get_http():
    if request.method == 'GET':
        # Waiting for something like 'http://127.0.0.1:5000/get.html/submit?username=Ivan'
        # Where username is the id attribute of a text field from the HTML form
        username = request.args.get('username')
        users = User.get_user(username)
        if users:
            first_str = 'Information from {}:'.format(username)
            second_str = ""
            for user in users:
                second_str += "\n - {}".format([user.id,
                                                user.username,
                                                user.password,
                                                user.age])
            return first_str + second_str
        return 'The data entered was not found'
    else:
        return 'Not supported http method: {}'.format(request.method)


@app.route('/post.html/submit', methods=['POST'])
def post_http():
    if request.method == 'POST':
        # When using POST method, the values are not passed as arguments in the URL. Therefore, we
        # use 'request.form' instead of 'request.args'
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age')
        user = User.post_user(username, password, age)
        if user:
            user_information = [
                user.id, user.username, user.password, user.age]
            return 'Information inserted:\n - {}:'.format(user_information)
        return 'Error'
    else:
        return 'Not supported http method: {}'.format(request.method)


@app.route('/put.html/submit', methods=['POST', 'PUT'])
def put_http():
    # Using an HTML form is not possible to use the method PUT
    # So, this function will be activated with the method PUT from HTML
    if request.method == 'POST' or request.method == 'PUT':
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age')
        user = User.put_user(username, password, age)
        if user:
            user_information = [
                user.id, user.username, user.password, user.age]
            return 'Information inserted:\n - {}:'.format(user_information)
        return 'Error'
    else:
        return 'Not supported http method: {}'.format(request.method)


@app.route('/delete.html/submit', methods=['GET', 'DELETE'])
def delete_http():
    # Using an HTML form is not possible to use the method DELETE
    # So, this function will be activated with the method GET from HTML
    if request.method == 'GET' or request.method == 'DELETE':
        username = request.args.get('username')
        password = request.args.get('password')
        age = request.args.get('age')
        user = User.delete_user(username, password, age)
        if user:
            user_information = [user.id, user.username, user.password, user.age]
            return 'Information deleted:\n - {}:'.format(user_information)
        return 'Error'
    else:
        return 'Not supported http method: {}'.format(request.method)


# Run the server always in debug mode allowing changes to be applied in real time.
if __name__ == '__main__':
    app.run(debug=True)
