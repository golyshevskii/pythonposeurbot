import os

bot_token = os.getenv('bot_token')
app_name = os.getenv('app_name')
app_url = f'https://{app_name}.herokuapp.com/' + bot_token
