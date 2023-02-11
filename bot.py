import logging
import logging.config
from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

from plugins.webcode import bot_run
from os import environ
from aiohttp import web as webserver

PORT_CODE = environ.get("PORT", "8080")

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       
       client = webserver.AppRunner(await bot_run())
       await client.setup()
       bind_address = "0.0.0.0"
       await webserver.TCPSite(client, bind_address, PORT_CODE).start()
       
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)                  
            self.invitelink = link
         except Exception as e:
            logging.warning(e)
            logging.warning("Make Sure Bot admin in force sub channel")             
            self.force_channel = None      
       logging.info(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
      

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped")
        
bot = Bot()
bot.run()
