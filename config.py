class Config:
    pass

class DevelopmentConfing(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:Panama.*@localhost:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfing(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:Panama.*@localhost:5432/api_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    

config = {
    'test': TestConfing,
    'development': DevelopmentConfing
}   