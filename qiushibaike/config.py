import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'a n string haha aha'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASK_MAIL_SUBJECT_PREFIX = '[glrh11]'
	FLASK_MAIL_SENDER = 'glrh11 <glrh11_test@163.com>'
	FLASK_ADMIN = os.environ.get('FLASK_ADMIN') or 'glrh11_test@163.com'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'glrh11_test@163.com'
	MAIL_PASSWORD = 'qwe123' #'os.environ.get('MAIL_PASSWORD')'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,

'default': DevelopmentConfig
}
