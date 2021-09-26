import discord
import sys
import os
from discord.ext import commands
from to import Token
import asyncio  #비동기 함수 호출

client = discord.Client()  #discord.Client()를 한번에 줄여줌

embed = discord.Embed(title="Embed", description="Embed 내용.", color=0x00aaaa)  # Embed를 선언해줌

dirctory = os.path.dirname(__file__)  #현 파이썬 모듈의 디렉토리 주소를 dirctory에 저장
file = discord.File(dirctory + "\\text.txt")  #dirctory 디렉터리 내에 있는 텍스트 파일을 file에 지정함

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)  #봇 이름 호출
    print("디스코드봇 ID:" + str(client.user.id))  #봇 id 호출
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('열공')) # 봇의 상태를 설정해주는 명령어(온라인, 자리비움, 다른 용무 중, 오프라인으로 설정하는것 )

@client.event
async def on_message(message):
    embed.set_author(name="작성자의 이름", icon_url=message.author.avatar_url)  #Embed 맨 윗값 선언
    embed.set_footer(text="이것은 footer의 값입니다.")  #Embed 맨 아랫값 선언
    embed.add_field(name="이것은 field입니다.", value="시험 중이에요", inline=False) #Embed 필드 값 선언
    content = message.content  #사용자가 보낸 내용을 표시
    guild = message.guild  #보낸 서버 이름을 표시
    author = message.author  #보낸 유저의 태그까지 포함해서 표시
    channel = message.channel  #보낸 유저의 채널을 표시
    if content.startswith("!test"):
        await message.channel.send("test" + message.content)
    if content == "!ping":
        await message.channel.send("이것은 TTS 테스트라고 합니다!",tts=True)
    if content == "!파일":
        await message.channel.send("임시 텍스트 파일",file=file)  #파일 전송
    if content.startswith("!도움"):
        await message.channel.send(embed=embed)  #Embed 출력
    if content.startswith("!따라하기"):
        answer = message.content[6:]  #!따라하기 이후 저장되는 context의 인덱스 값 6에서부터 answer를 저장함
        await message.channel.send(answer)  #출--력
    if content.startswith("!내용"):
        msg_l = content.split()  #입력 받은 값들을 공백 단위로 분리시켜 저장해 줌.
        try:
            data = msg_l[1]  #msg_l중 2번째 리스트 값을 저장
        except:  #입력 예상에서 벗어날 시(내용을 입력하지 않았을 때)
            await channel.send("내용을 입력해주세요!")
            return
        await channel.send(data)  #출--력

@client.event
async def on_error(event, *args, **kwargs):  #실행중 에러 발생 시(event: on_message 반환, *args: 그 message를 돌려줌 **kwargs: 예외를 발생시킨 이벤트에 대한 키워드 인수(사실 에러 값은 sys.exc_info에서 알 수 있다고 함.(거의 사용 안한다고 보면 됨))
    if event == "on_message": #on_message에서 에러가 발생했을 때 작동
        message = args[0]  #args값에는 여러개가 들어올 수도 있으니, 첫번째 것만 잡아줌
        exc = sys.exc_info()  #sys를 활용하여 에러를 확인함
        message.channel.send(str(exc[0].__name__) + "" + str(exc[1]))  #해당 에러를 출력
    return

@client.event
async def on_typing(channel, user, when):  #유저가 타이핑 중일 때 나타나는 이벤트
    await channel.send(str(user) + "이 작성중!")  #어떤 user가 타이핑 중인지 출--력
    return

@client.event
async def on_guild_join(guild):
    print()

client.run(Token) #보안을 위해 다른 코드(to.py)에서 토큰 값을 가져옴