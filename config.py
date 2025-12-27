class Config:
    DEBUG= False
    DATABASE_SERVER = "54.67.89.17"
    SECRET_KEY= 123

class Development(Config):
    DEBUG= False
    SECRET_KEY= 456
class Testing(Config):
    DEBUG= True
    SECRET_KEY= 789