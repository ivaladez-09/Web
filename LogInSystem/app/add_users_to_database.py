"""Adding first elements to the db"""
from app import db
from app.models import User


if __name__ == '__main__':

    u = User(username='ivan', password='123', age=24)
    db.session.add(u)
    u = User(username='susana', password='321', age=24)
    db.session.add(u)
    u = User(username='aaron', password='789', age=19)
    db.session.add(u)
    db.session.commit()

    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.password, u.age)
