class BaseConfig():
    SCRET_KEY = 'secret_key'


class DevelopmentConfig(BaseConfig):
    DEBUG=1
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/hanhan?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
            'development': DevelopmentConfig,
            'production': ProductionConfig,
            'Testing' : TestingConfig
        }
