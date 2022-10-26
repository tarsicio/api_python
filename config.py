class Config:
	pass

class DevelopmentConfing(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI ='postgresql://localhost/api'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
	'development': DevelopmentConfing
}	