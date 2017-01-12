#coding:utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess key'
    SQLACHEMY_COMMIT_ON_TRARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'guocqmail@163.com'
    FLASK_ADMIN = FLASK_MAIL_SENDER

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USENAME = os.environ.get('mail_name')
    MAIL_PASSWORD = os.environ.get('mail_pswd')

    SQLACHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USENAME = os.environ.get('mail_name')
    MAIL_PASSWORD = os.environ.get('mail_pswd')

    SQLACHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data-test.sqlite')


class ProductionConfig(Config):

    SQLACHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')


Config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}


