import os


class Config(object):
	FLASK_ENV = 'development'
	DEBUG = False
	TESTING = False
	SECRET_KEY = os.getenv('SECRET_KEY', default=b'\xa2\xc2\x9e\x87P\xc8bv&0\xb3r`\xf4\x1d\x00\x95\x8f\x08E\x85\xe7\xc4\x97\xc0]\xa6\xa8\xb2\x1d %\xf6')

class ProductionConfig(Config):
	FLASK_ENV = 'production'

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
