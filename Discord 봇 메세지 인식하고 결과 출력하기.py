#Discord 봇 메세지 인식하고 결과 출력하기.py
import asyncio
import discord 
client = discord.Client

#생성된 토큰 입력
Data = "토큰정보" #봇의 토큰 정보 입력

@client.event
async def bot_start():
    print("다음 정보로 로그인을 시도합니다.")
    print(client.user.name)
    print(client.user.id)
    print("============================================")

#봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message): #메세지를 보낸 사람이 봇일 경우애는 무시한다.

if message.author.bot:
    return None
if message.content.startswith("안녕"):

channel = message.channel
    await channel.send("반가워")
    client.run(Data) #실행
