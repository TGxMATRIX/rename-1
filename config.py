import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "19376711")

API_HASH = os.environ.get("API_HASH", "97d6b9d4999508a0c29d71c348d33351")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5814516485:AAGPJx5Neje4DVg3aGaGeknFkShWRjQ2o1Y") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MatRixBotzTG") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://ok:ok@cluster0.hsirmld.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/c1159039f103f9a9b4506.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1580642587').split()]

