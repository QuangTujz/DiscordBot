import discord
import random
from datetime import *
from discord.ext import commands

client=commands.Bot(command_prefix='.',status=discord.Status.idle,activity=discord.Game("with his friends"))

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_member_join(member):
    print(f"{member} da vao` server nay`. Hello {member}")

@client.event
async def on_member_left(member):
    print(f"{member} da roi` khoi server. Cut' di nhanh")

@client.command() #Lệnh ping
async def ping(ctx):
    embed=discord.Embed(
        title = "Ping",
        description = (f'{round(client.latency*1000)}ms'),
        color=discord.Color.from_rgb(87,232,226)
    )
    await ctx.send(embed = embed)

@client.command() #Lệnh hungphi
async def hungphi(ctx):
    embed=discord.Embed(
        title='Bot Hùng Phi',
        description='Bot mạnh nhất server này!',
        color=discord.Color.from_rgb(107,37,189)
    )
    embed.set_author(name='Nguyễn Quang Tú', icon_url='https://i.pinimg.com/564x/56/f7/c6/56f7c6e3900a943c507a41bfb0d94a61.jpg')
    embed.set_image(url='https://i.redd.it/xl8ppc0pnw881.png')
    embed.set_footer(text='Đang cải thiện bot này...')
    embed.set_thumbnail(url='https://i.pinimg.com/564x/56/f7/c6/56f7c6e3900a943c507a41bfb0d94a61.jpg')
    embed.add_field(name='.ping', value='Check ping bot (Thông thường hơi cao)')
    embed.add_field(name='.users', value='Check có bao nhiêu người',inline=True)
    embed.add_field(name='.randomnumber', value='Random từ 1-100',inline=True)
    embed.add_field(name='.cauhoi (Câu hỏi)', value='Đặt bot một câu hỏi',inline=True)
    embed.add_field(name='.time', value='Current time', inline=True)
    await ctx.send(embed=embed)


@client.command() #Lệnh users
async def users(ctx):
    id_server=client.get_guild(892359590166020137)
    embed=discord.Embed(
        title = "Users",
        description = (f'Có tất cả {id_server.member_count} thành viên trong server'),
        color=discord.Color.dark_blue()
    )
    await ctx.send(embed=embed)

@client.command(pass_context = True) #Lệnh random
async def randomnumber(ctx):
    embed=discord.Embed(title = "Random từ 1-100", description = (random.randint(1,101)),color=0xF44336)
    await ctx.send(embed=embed)

@client.command() #Lệnh time
async def time(ctx):
    current = datetime.now().strftime("%d/%m/%Y %H:%M")
    embed = discord.Embed(
        title = "Giờ hiện tại",
        description = (current),
        color = discord.Color.from_rgb(35,242,228)
    )
    await ctx.send(embed = embed)

@client.command(aliases=['cauhoi','test']) #Lệnh cauhoi
async def _cauhoi(ctx,*,question):
    responses = ['Đương nhiên là có',
                'Chưa biết được',
                'Chắc chắn 100%',
                'Hiển nhiên rồi',
                'Ai mà biết được',
                'T cũng không biết',
                'Tùy',
                'T cũng không chắc chắn lắm',
                'M hỏi thế ai mà trả lời được',
                '...',
                'Không trả lời được',
                'Phụ thuộc vào một số trường hợp',
                'Câu hỏi khó thế, hỏi câu khác đi',
                'Cũng chưa chắc chắn',
                'Sao m lại hỏi câu đấy?',
                'Thôi. Hỏi ít thôi bạn',
                'Bạn bị làm sao đấy???',
                '🤪',
                'Câu hỏi này không có câu trả lời',
                'Bỏ qua câu này đi. T không muốn trả lời đâu nhé']
    await ctx.send(f'{random.choice(responses)}')

@client.command() #lệnh gayrate
async def gayrate(ctx):
    ran_dom = random.randint(0,120)
    sentence = ""
    if ran_dom > 100:
        sentence = (f"{ctx.author.mention} vượt quá 100%. Thằng này gay vcl")
    else:
        sentence = (f"{ctx.author.mention} có độ gay là {ran_dom}%")
    embed = discord.Embed(
        title = 'Tính độ gay',
        description = sentence,
        color = discord.Color.from_rgb(0,0,0)
    )
    await ctx.send(embed = embed)


@client.command() #Lệnh clear
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)


client.run('') // Insert your bot token here
