from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cmd to run server: poetry run flask --app todo run -p 6400 --debug 
#Cmd to inspect database: sqlite3 instance/db.sqlite

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    
    if config_overrides: 
      app.config.update(config_overrides)

    # Load the models 
    from todo.models import db 
    from todo.models.todo import Todo 
    db.init_app(app) 

    # Create the database tables 
    with app.app_context(): 
      db.create_all() 
      db.session.commit() 

    # Register the blueprints
    from todo.views.routes import api
    app.register_blueprint(api)

    return app
