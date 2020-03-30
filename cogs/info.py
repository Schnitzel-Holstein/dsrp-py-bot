import discord
from discord.ext import commands

class Información(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Info\'s commands: OK')

    #@commands.command()
    #async def ping(self, ctx):
    #    await ctx.send(f'Tu ping es de {round(commands.Bot.latency*1000)}ms')


def setup(client):
    client.add_cog(Información(client))