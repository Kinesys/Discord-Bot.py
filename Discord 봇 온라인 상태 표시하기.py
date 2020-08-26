#Discord 봇 온라인 상태 표시하기.py
import discord 
import asyncio
client = discord.client

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("Bot Start")
game = discord.Game("Battle Ground")
await client.change_presence(status=discord.status.idle, activity=game)
client.run("봇의 토큰값") #봇의 토큰값 
