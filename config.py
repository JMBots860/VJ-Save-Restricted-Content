import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22525785"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c7bf5043d649807ea7c66ac045a49ae3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vishaldebejob:OHlXUHOOSYhml18G@cluster0.f2omf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
