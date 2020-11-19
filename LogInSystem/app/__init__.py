""""""
from flask import Flask, render_template, request, url_for, redirect
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Add our configuration to the app configuration
app.config.from_object(config.Config)
# Creating objects for the database an migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# To create the migration repo, in terminal write "flask db init"
# Create the db "flask db migrate -m "users table""
# Update th db "flask db upgrade"

# This has to be added at the end
from app import routes, models
