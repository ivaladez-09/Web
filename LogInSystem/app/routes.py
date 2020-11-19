""""""
from app import app, render_template, request, url_for, redirect, db
from app.models import User


@app.route('/')
@app.route('/index.html')
def index():
    """"""
    return render_template('index.html', title='LogIn')


@app.route('/submit', methods=['GET'])
def login():
    """"""
    if request.method == 'GET':
        # /login?username=ivan&password=123
        username = request.args.get('username')
        password = request.args.get('password')

        if username and password:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                user = [user.id, user.username, user.password, user.age]
                return '\n\t{}, {}, {}, {}'.format(*user), 202  # 202 = Accepted

        return 'User not registered', 401  # 401 = Unauthorized

    return 'Wrong method {}'.format(request.method), 400  # 400 = Bad request


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/submit', methods=['POST'])
def register_submit():
    """"""
    if request.method == 'POST':
        # /login?username=ivan&password=123&age=24
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age')

        if username and password and age:
            user = User.query.filter_by(username=username, password=password, age=age).first()
            if not user:  # User not yet added
                user = User(username=username, password=password, age=age)
                db.session.add(user)
                db.session.commit()

                user = [user.id, user.username, user.password, user.age]
                return '\n\tUser registered: {}, {}, {}, {}'.format(*user), 202  # 202 = Accepted
            else:
                return '\n\tUser already registered.'

        return 'Complete all the fields', 401  # 401 = Unauthorized

    return 'Wrong method {}'.format(request.method), 400  # 400 = Bad request
