import discord
import sys
import os
import asyncio
from to import Token

client = discord.client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)  # 봇 이름 호출
    print("디스코드봇 ID:" + str(client.user.id))  # 봇 id 호출
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online,activity=discord.Game('열공'))  # 봇의 상태를 설정해주는 명령어(온라인, 자리비움, 다른 용무 중, 오프라인으로 설정하는것 )

@client.event
async def on_member_join(member):
    await member.guild.get_channel("890628038893666357").send(member.mention + "님 저희 삼칠아파트에 주거하시게 되신걸 환영합니다! 👋  먼저 아파트 게시판의 공지사항을 보러 가주세요!")

@client.event
async def on_member_remove(member):
    await member.guild.get_channel("891161943778418699").send(member + "님 저희 삼칠아파트 에서 떠나시는군요! 😂 다른 아파트에서도 잘 사시길 바래요!")

client.run(Token)