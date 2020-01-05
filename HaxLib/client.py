import requests

api = 'https://discordapp.com/api/v6'

class client(object):
    def __init__(self, token):
        self.token = token

    def send_msg(self, channel_id, msg:str):
        url = api + f'/channels/{str(channel_id)}/messages'
        payload = {
          "content": msg
          }
        headers = {
          "Authorization":f"Bot {self.token}"
          }
        r = requests.post(url=url, headers=headers, json=payload)
        print(r.text)

    def send_embed(self, channel_id, desc, title=''):
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
        print(r.text)
