import discord
import random
from discord.ext import commands


class Diversión(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun\'s commands: OK')

    @commands.command(aliases=['8ball', 'answer', 'ans'])
    async def _8ball(self, ctx, *, pregunta):
        respuestas = [
        'En mi opinión, sí',
        'Es cierto',
        'Es decididamente así',
        'Probablemente',
        'Buen pronóstico',
        'Todo apunta a que sí',
        'Sin duda',
        'Sí',
        'Definitivamente',
        'Debes confiar en ello',
        'Respuesta vaga, vuelve a intentarlo',
        'Pregunta en otro momento',
        'Será mejor que no te lo diga ahora',
        'No puedo predecirlo ahora',
        'Concéntrate y vuelve a preguntar',
        'Puede ser',
        'No cuentes con ello',
        'Mi respuesta es no',
        'Mis fuentes me dicen que no',
        'Las perspectivas no son buenas',
        'Muy dudoso']
        await ctx.send(f'Pregunta: {pregunta}\nRespuesta: {random.choice(respuestas)}')


def setup(client):
    client.add_cog(Diversión(client))