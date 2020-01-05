import requests

api = 'https://discordapp.com/api/v6'

class client:
    def login(token):

    headers = {
        'Authorization':f'Bot {token}'
        }
    requests.get(url=api, headers=headers)
