from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24906331")
    API_HASH = environ.get("API_HASH", "866e8e4637fb269388b50202fb0f169c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7466801582:AAHdPM1H8SUmwaz69C8TWKzgsmUtFxy7qrs") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6290315686').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
