# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21593885"))
    API_HASH = getenv("API_HASH", "66c868b925a30a3deb21c300a69d1425")
    BOT_TOKEN = getenv("BOT_TOKEN", "7048774458:AAHSkpcWvyU6sfY09EJnPQahK_7EDgj7HYo")
    FSUB = getenv("FSUB", "The_Movies_Officially")
    CHID = int(getenv("CHID", "-1001891085801"))
    SUDO = list(map(int, getenv("SUDO", "7051286976").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rename72:khan7860@cluster0.eds4g6b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
