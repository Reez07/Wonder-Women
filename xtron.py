"""import discord
import os
import json
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startwith('hello'):
        await message.channel.send('hi')

client.run('MTA1MzU0NTA4NTI5MzMxODIzNg.G0yv4j.EHxltx9vK0L0f4QR5I3-r81hpETJkZcs1REMNY')
http://localhost:8000/api/random/
http://localhost:8000/admin/ 
"""

import bot

if __name__ == '__main__':
    bot.run_discord_bot()
