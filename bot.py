import discord
from discord.ext import commands
from to import Token
import asyncio  #비동기 함수 호출

client = discord.Client()  #discord.Client()를 한번에 줄여줌

embed = discord.Embed(title="Embed", description="Embed 내용.", color=0x00aaaa)  # Embed를 선언해줌

bot=commands.Bot(command_prefix='*')  #prefix + 사용할 명령어를 붙여주면 작동함

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)  #봇 이름 호출
    print("디스코드봇 ID:" + str(client.user.id))  #봇 id 호출
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('열공')) # 봇의 상태를 설정해주는 명령어(온라인, 자리비움, 다른 용무 중, 오프라인으로 설정하는것 )

@client.event
async def on_message(message):
    embed.set_author(name="작성자의 이름", icon_url=message.author.avatar_url)  #Embed 맨 윗값 선언
    embed.set_footer(text="이것은 footer의 값입니다.")  #Embed 맨 아랫값 선언
    embed.add_field(name="이것은 field입니다.", value="이것은 field 값입니다.", inline=False) #Embed 필드 값 선언
    content = message.content  #사용자가 보낸 내용을 표시
    guild = message.guild  #보낸 서버 이름을 표시
    author = message.author  #보낸 유저의 태그까지 포함해서 표시
    channel = message.channel  #보낸 유저의 채널을 표시
    if content.startswith("!test"):
        await message.channel.send("test" + message.content)
        await message.channel.send(embed=embed)  #Embed 출력
    if content == "!ping":
        await message.channel.send("Pong!")


client.run(Token) #보안을 위해 다른 코드(to.py)에서 토큰 값을 가져옴