import discord
from discord.ext import commands


class Moderación(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Mod\'s commands: OK')

    @commands.command()
    async def borrar(self, ctx, monto=5):
        await ctx.channel.purge(limit=monto + 1)

    @commands.command()
    async def kick(self, ctx, member: discord.member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member: discord.member, *, reason=None):
        await member.ban(reason=reason)


def setup(client):
    client.add_cog(Moderación(client))