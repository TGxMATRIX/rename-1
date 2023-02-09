import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11615722")

API_HASH = os.environ.get("API_HASH", "c992746520e8886d3330de2ec9a1a3a7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6225376312:AAHwyKTaYHVGdJdJwPHt4b_Aw7-YEpkAQEc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MatRixBotzTG") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://re:re@cluster0.julflp9.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/c1159039f103f9a9b4506.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5596825598').split()]

