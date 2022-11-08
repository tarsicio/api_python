class Config:
    pass

class DevelopmentConfing(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:Panama.*@localhost:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfing
}   