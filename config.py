import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config():
    """
        Set Config variables for the flask app.
        Using Enviornment variables where available, otherwise;
        create the config variable if not done already.
    """
    FLASK_APP = os.getenv('FLASK_APP')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Itheann tu an ceapaire'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get('FLASK_DEBUG') == '1'