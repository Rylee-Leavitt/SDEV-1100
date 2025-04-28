#
# Rylee Leavitt
# 4/27/25
# SDEV1100 1st project
# SDEV 1100
#

#__init__.py
#Flask tutorial

#create_app is the application factory function.
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) 
    #app = Flask(__name__, instance_relative_config=True) creates the Flask instance.
    #__name__ is the name of the current Python module. 
        # The app needs to know where it’s located to set up some paths
    #instance_relative_config=True tells the app that configuration files are relative to the instance folder. 

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        #app.config.from_mapping() sets some default configuration that the app will use
            #SECRET_KEY is used by Flask and extensions to keep data safe.
            #DATABASE is the path where the SQLite database file will be saved. It’s under app.instance_path
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing

        app.config.from_pyfile('config.py', silent=True)
        #app.config.from_pyfile() overrides the default configuration
        #with values taken from the config.py file in the instance folder if it exists.

        
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        #os.makedirs() ensures that app.instance_path exists. Flask doesn’t create the instance folder automatically, 
        #but it needs to be created because your project will create the SQLite database file there.

    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    #@app.route() creates a simple route 
    
    def hello():
        return 'Hello, World!'

    return app

#
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app

#Initialize the Database File
    #$ flask --app flaskr init-db
    # Initialized the database.
    #There will now be a flaskr.sqlite file in the instance folder in your project.