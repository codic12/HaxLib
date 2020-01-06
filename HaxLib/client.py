import requests
import json

api = 'https://discordapp.com/api/v7'

class client(object):
    def __init__(self, token):
        self.token = token
        self.headers = {
          "Authorization":f"Bot {self.token}"
          }

    async def send_msg(self, channel_id, msg:str):
        url = api + f'/channels/{str(channel_id)}/messages'
        payload = {
          "content": msg
          }

        r = requests.post(url=url, headers=self.headers, json=payload)
        return json.loads(r.text)
        
    async def send_embed(self, channel_id, desc, title=''):
        url = api + f'/channels/{str(channel_id)}/messages'
        payload = {
          "embed": {
            "title": title,
            "description": desc
            }
          }
        r = requests.post(url=url, headers=self.headers, json=payload)
        return json.loads(r.text)
        
    async def edit_msg(self, message, new_msg):
        message_id = message["id"]
        channel_id = message['channel_id']
        payload = {
          "content":new_msg
          }
        url = api + f'/channels/{str(channel_id)}/messages/{str(message_id)}'
        requests.post(url=url, headers=self.headers, json=payload)

    async def get_msg(self, channel_id, message_id):
        url = api + f'/channels/{str(channel_id)}/messages/{str(message_id)}'
        return json.loads(requests.get(url=url, headers=self.headers).text)

    async def react(self, message, emoji):
        channel_id = message['channel_id']
        message_id = message['id']
        url = api + f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me'
        return requests.post(url=url, headers=self.headers).text

    async def create_inv(self, channel_id, max_uses=0, max_age=0):
        payload = {
          'max_uses':max_uses,
          'max_age':max_age
          }
        url = api + f'/channels/{str(channel_id)}/invites'
        return f'https://discord.gg/{json.loads(requests.post(url=url, headers=self.headers, json=payload).text)["code"]}'
