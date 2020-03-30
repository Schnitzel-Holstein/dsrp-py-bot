import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='=')


@client.event
async def on_ready():
    print('Bot: OK')


@client.event
async def on_member_join(member):
    print(f'{member} ha entrado al servidor. ¡Denle la bienvenida!')


@client.event
async def on_member_remove(member):
    print(f'{member} ha salido del servidor.')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('NjkxNzEwNjcxNTQwMTkxMjky.Xnj7yw.F0CzjQUSwoy3YBAA0OeBy_cvW3E')
