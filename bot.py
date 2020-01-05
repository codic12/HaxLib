from HaxLib import client

with open('token.txt') as f:
    HaxBotToken = f.read()
    f.close()

HaxBot = client(HaxBotToken)

while True:
    q = input('Would you like to send an embed or normal msg? ').lower()
    channel_id = int(input('Enter the channel ID that you want to send this message to: '))
    if q == 'embed':
        HaxBot.send_embed(channel_id, input('Please enter a title for the embed: '), input('Please enter a description for the embed: '))
    elif q == 'normal':
        HaxBot.send_msg(channel_id, input('Please enter a message to send: '))
