from os import environ 


class config:
  '''Set Flask configuration vars from .env file.'''
  #GENERAL CONFIG
  SECRET_KEY = environ.get('SECRET_KEY')
  FLASK_APP = environ.get('FLASK_APP')
  FLASK_ENV = environ.get('FLASK_ENV')
  FLASK_DEBUG = environ.get('FLASK_DEBUG')

  #DATABASE
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=
  os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')