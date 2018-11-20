
import os
import errno
import datetime
import logging
from telethon import utils
from telethon import TelegramClient, sync
from telethon.tl.types import InputMessagesFilterDocument


## SETTINGS

NUM_FILES = 10
CHANNEL_NAME = "@MagazinezWorld"
API_ID = ""
HASH = ""
SESSION_NAME = ""

#logging.basicConfig(level=logging.DEBUG)

# If you change the session name - it will require 2 factor authentication again.

def main(api_id = API_ID
        ,api_hash = HASH
        ,session_name = SESSION_NAME):

    # TODO Ask to download specific files [message.download_media(filename)]
    # TODO limit by date [?]
    # TODO Create a folder for each date.
    # TODO Test IP to see if Telegram is up?
    # TODO Create renaming function.
    
    # Perform a clear screen.
    os.system('cls')

    # Establish Client
    client = TelegramClient(session_name,api_id,api_hash)

    try:             
        # Start Client
        client.start()        
        # Channel name string
        channel_name = "@MagazinezWorld"
        # Iterate through all the messages and download the attachments.
  
        
        #This loop check
        for message in client.iter_messages(CHANNEL_NAME, NUM_FILES, filter=InputMessagesFilterDocument):
            atri = message.media.document.attributes
            print("IDm: ", message.id)
           #print("ID by 2:", message)
            print("Message: ", message.message)
            print("Date:", message.date)
            print("Size:" , message.media.document.size)
            print("File name:" , atri[0].file_name, "\n")

    finally:
        # client.logout() will require a new session authentication
        # so we just disconnect in order to suse the same. 
        client.disconnect()

if __name__ == '__main__':
    main()
