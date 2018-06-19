import config
import discord
import asyncio
import urllib3
import certifi
import idna
import requests
import tools

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name=config.prefix+'help'))
    print('------')

@client.event
async def on_message(message):
    if message.author.name != client.user.name:
        if message.content.startswith(config.prefix+'help'):
            await client.send_message(message.channel,
                                      message.author.mention+" Here's some commands you can use:\n"
                                      +config.prefix+"account <Username> - shows player stats\n"
                                      +config.prefix+"link - get link to add bot to your server\n")
        elif message.content.startswith(config.prefix+'account'):
            username = message.content.replace(config.prefix+'account ','')
            acc = tools.getAccount(username)
            if acc != -1:
                await client.send_message(message.channel, message.author.mention+", here's stats for user "+username+':\n'+tools.getAccountInfo(acc))
            else:
                await client.send_message(message.channel, "Error! Maybe there is no user with nickname: "+username)
        elif message.content.startswith(config.prefix+'link'):
            await client.send_message(message.channel,message.author.mention+" Use this link to connect me to your server: \n"+discord.utils.oauth_url(client.user.id, permissions=None, server=None, redirect_uri=None))
client.run(config.token)
