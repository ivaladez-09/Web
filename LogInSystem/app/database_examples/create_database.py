"""Adding first elements to the db"""
from app import db
from app.models import User, Post


if __name__ == '__main__':

    u = User(username='john', email='john@example.com')
    db.session.add(u)
    u = User(username='susan', email='susan@example.com')
    db.session.add(u)
    db.session.commit()

    users = User.query.all()
    for u in users:
        print(u.id, u.username)  # 1 john ...

    u = User.query.get(1)
    p = Post(body='my first post!', author=u)
    db.session.add(p)
    db.session.commit()

    # get all posts written by a user
    u = User.query.get(1)
    posts = u.posts.all()

    # same, but with a user that has no posts
    u = User.query.get(2)
    u.posts.all()

    # print post author and body for all posts 
    posts = Post.query.all()
    for p in posts:
        print(p.id, p.author.username, p.body)

    # get all users in reverse alphabetical order
    User.query.order_by(User.username.desc()).all()

    users = User.query.all()
    for u in users:
        db.session.delete(u)

    posts = Post.query.all()
    for p in posts:
        db.session.delete(p)

    db.session.commit()