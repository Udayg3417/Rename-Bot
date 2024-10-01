import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "21562110"))
API_HASH = os.environ.get("API_HASH", "4d1e1f333214a39cea79a3196cbed290")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6909056240"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1001902643858")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002310797087"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://guday3417:GUDAY333@cluster0.pdrwfcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "")
