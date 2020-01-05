import requests
import json

api = 'https://discordapp.com/api/v6'

class client(object):
    def __init__(self, token):
        self.token = token

    async def send_msg(self, channel_id, msg:str):
        url = api + f'/channels/{str(channel_id)}/messages'
        payload = {
          "content": msg
          }
        headers = {
          "Authorization":f"Bot {self.token}"
          }
        r = requests.post(url=url, headers=headers, json=payload)
        return json.loads(r.text)

    async def send_embed(self, channel_id, desc, title=''):
        url = api + f'/channels/{str(channel_id)}/messages'
        payload = {
          "embed": {
            "title": title,
            "description": desc
            }
          }
        headers = {
          "Authorization":f"Bot {self.token}"
          }
        r = requests.post(url=url, headers=headers, json=payload)
        return json.loads(r.text)

    async def edit_msg(self, message, new_msg):
        message_id = message["id"]
        channel = message['channel_id']
        headers = {
          "Authorization":f"Bot {self.token}"
          }
        payload = {
          "content":new_msg
          }
        url = api + f'/channels/{str(channel_id)}/messages/{str(message_id)}'
        requests.post(url=url, headers=headers, json=payload)
