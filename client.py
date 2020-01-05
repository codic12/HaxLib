import requests

api = 'https://discordapp.com/api/v6'

class client(token):
    def send_msg(channel_id, msg:str):
        headers = {
          "Authorization":f"Bot {token}",
          "content": f"{msg}",
          "tts": false,
           "embed": {
            "title": "Hello, Embed!",
            "description": "This is an embedded message."
          }
        }        
