import os

class Config:
    DEBUG= False
    SECRET_KEY= os.getenv("SECRET_KEY")
    API_BASE=os.getenv("API_BASE")


class Development(Config):
    DEBUG= False
    SECRET_KEY= 456
    API_BASE="prod.server.com"
class Testing(Config):
    DEBUG= True
    SECRET_KEY= 789