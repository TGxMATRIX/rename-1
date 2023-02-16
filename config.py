import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11615722")

API_HASH = os.environ.get("API_HASH", "c992746520e8886d3330de2ec9a1a3a7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6091563147:AAFKAQL8MRj4E7gLKvQmYpi_Jg4KnJGNaJs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MLZ_BOTZ") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://re:re@cluster0.julflp9.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/8a370dfcfaf98070af522.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5596825598 5726662425 5845960615 1833209093').split()]

PORT = os.environ.get('PORT', '8080')

LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001745143192'))
