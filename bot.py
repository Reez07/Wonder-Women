import discord
import responses
import os
import json
import random
import requests
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN ='token'

trigger_words = ["I'm bored", "!motivate-me"]
inspiration = ["You can do it!","Don't give up!","Just keep going,Just keep going, Just keep,Just keep, Just keep going!🐟"," \“And, when you want something, all the universe conspires in helping you to achieve it.\”―Paulo Coelho", "The Alchemist \“Dreams don\'t work unless you do.\” ―John C. Maxwell", "\“Go the extra mile. It\'s never crowded there.\” ―Dr. Wayne D. Dyer","\“Keep your face always toward the sunshine―and shadows will fall behind you.\” ―Walt Whitman", "\“What defines us is how well we rise after falling.\” ―Lionel"]
dictionary = {"Periodic Motion":"Any motion which repeats itself at regular intervals of time."}
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
            guess = await client.wait_for('message', check=check, timeout=7.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Uh oh! Timeout.⏰')   
        if int(guess.content) == answer:
            await message.channel.send('Wohoo! You got it right.🥳')
        else:
            await message.channel.send('Woops! Better luck next time.💔')
    if any (word in message.content for word in trigger_words):
        phrases = inspiration
        await message.channel.send(random.choice(phrases))
""" if message.content.startswith("!define"):
        word = message.content
        word = slice[7:]
        print(word)
        for key in dictionary.keys():
            if word == key:
             await message.channel.send(dictionary[key]) """
""" if message.content.startswith('!addquestion'):
            await message.channel.send('Enter the question')
            quest = message.content"""
            


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
    TOKEN = 'tokenI'
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
