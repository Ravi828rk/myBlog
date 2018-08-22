import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '787237187238HDAJHDJSH87381723'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25) or 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'flasktestingemail@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'golumolu@12345'
    ADMINS = ['ravi828.rk@gmail.com']
