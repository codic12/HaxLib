import requests

api = 'https://discordapp.com/api/v6'

class client(object):
    def __init__(self, token):
        self.token = token
    def send_msg(self, channel_id, msg:str):
        url = api + f'/channels/{channel_id}/messages'
        headers = {
          "Authorization":f"Bot {self.token}",
          "content": f"{msg}",
          "tts": 'false',
           "embed": {
            "title": "Hello, Embed!",
            "description": "This is an embedded message."
            }
          }        
        r = requests.get(url=url, headers=headers)
        print(r.text)
