import discord
import responses
import os
import json
import random
import discord
import requests
import json
import asyncio
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN =token'

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"
    for item in json_data[0]['answer']:
        qs += str(id) + "." + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        id += 1
    return(qs,answer)

@client.event
async def on_message(message):
   
    if message.author ==  client.user:
        return
    if message.content.startswith('!question'):
        qs,answer = get_question()
        await message.channel.send(qs)
        def check(m):
            return m.author == message.author and m.content.isdigit()
        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Timeout')   
        if int(guess.content) == answer:
            await message.channel.send('You got it right!')
        else:
            await message.channel.send('Try again')
client.run(TOKEN)

async def send_message(message, user_message, is_private):
    try:
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)    

def run_discord_bot():
    TOKEN = 'token'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message. channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
