import discord
from commands import commandes

intents = discord.Intents.all()
client = discord.Client(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Code pour la commande /contacter
    if message.author.id != client.user.id and (message.author.bot == False):
        if message.content.lower().startswith('/'):
            odd = lambda data: data['name'] == message.content[1:].split(' ')[0]
            next_function = next(filter(odd, commandes), None)
            if next_function != None:
                await next_function['do'](client, message, " ".join(message.content.split(' ')[1:]), message.content.split(' ')[1:])
            else:
                channel = await message.guild.get_member(message.author.id).create_dm()
                await channel.send('Commande Incorrecte !')
                await client.http.delete_message(message.channel.id, message.id)

client.run('NzY4NTY0MDA0MzI2NjA0ODcx.X5CTAQ.E65rxFfBFKxnXpf03z5w2xkUKx4')
