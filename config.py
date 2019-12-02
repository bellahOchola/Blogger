import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

	@staticmethod
	def init_app(app):
		pass

class TestConfig:
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:bellah@1972@localhost/blog_test'	


class ProdConfig(Config):
    pass
    


class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:bellah@1972@localhost/blog'

	DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test' :TestConfig
}
