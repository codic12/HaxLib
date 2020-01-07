from os import system

#system('python3 -m pip install -U https://github.com/HuyaneMatsu/hata/archive/master.zip')

del(system)

from hata import Client, start_clients, sleep

from hata.events import CommandProcesser, ContentParser

from HaxLib import client, embeds

import json

with open('token.txt') as f:

    HaxBotToken = f.read().strip('\n')

    f.close()

Gateway = Client(HaxBotToken)

HaxBot = client(HaxBotToken)

embeds = embeds.embeds

on_command = Gateway.events(CommandProcesser('hl:')).shortcut

from string import ascii_lowercase, ascii_uppercase

emojis = ['ðŸ‡¦', 'ðŸ‡§', 'ðŸ‡¨', 'ðŸ‡©', 'ðŸ‡ª', 'ðŸ‡«', 'ðŸ‡¬', 'ðŸ‡­', 'ðŸ‡®', 'ðŸ‡¯', 'ðŸ‡°', 'ðŸ‡±', 'ðŸ‡²', 'ðŸ‡³', 'ðŸ‡´', 'ðŸ‡µ', 'ðŸ‡¶', 'ðŸ‡·', 'ðŸ‡¸', 'ðŸ‡¹', 'ðŸ‡º', 'ðŸ‡»', 'ðŸ‡¼', 'ðŸ‡½', 'ðŸ‡¾', 'ðŸ‡¿']

stuff = dict(zip(ascii_lowercase, emojis))

stuff.update(dict(zip(ascii_uppercase, emojis)))

trans = str.maketrans(stuff)

def emojify(string: str, sep: str = '\u200b'):

    return sep.join(string.translate(trans))

@on_command

async def msg(client, message, content):

    await HaxBot.send_msg(message.channel.id, content)

@on_command

@ContentParser('str', 'rest')

async def embed_msg(client, message, text, content):

    await HaxBot.send_msg(message.channel.id, embed=embeds.create_embed(content, text))

@on_command

async def emojify(client, message, content):

    await HaxBot.send_msg(message.channel.id, emojify(content))

@on_command

@ContentParser('str', 'int', 'rest')

async def edit_msg(client, message, edit, message_id, content):

    if edit.lower() == 'true':

        message = await HaxBot.get_msg(message.channel.id, message_id)

    else:

        message = await HaxBot.send_msg(message.channel.id, "This is a test message")

        message_id = message['id']

    data = {

      'id':message_id,

      'channel_id': message['channel_id']

      }

    await sleep(2,Gateway.loop)

    await HaxBot.edit_msg(data, content)

@on_command

async def reaction_msg(client, message):

    message = await HaxBot.send_msg(message.channel.id, "I'ma react to my message")

    print(await HaxBot.react(message, '\xf0\x9f\x98\x82'))

@on_command

async def create_inv(client, message):

    await HaxBot.send_msg(message.channel.id, await HaxBot.create_inv(message.channel.id))

    print(await HaxBot.create_inv(message.channel.id))

start_clients()

