import discord

async def mute(client, message, content, params):
    if message.channel.id == 768227816335999010 and message.guild.get_role(768228665539428372) in message.author.roles:
        for member in message.guild.members:
            if member in message.guild.get_channel(768227816335999011).members:
                await member.edit(mute=True)
        await client.http.delete_message(message.channel.id, message.id)
async def unmute(client, message, content, params):
    if message.channel.id == 768227816335999010:
        for member in message.guild.members:
            if member in message.guild.get_channel(768227816335999011).members and message.guild.get_role(768228665539428372) in message.author.roles:
                await member.edit(mute=False)
        await client.http.delete_message(message.channel.id, message.id)



commandes = [
    {
        "name": "mute",
        "do": mute
    },
    {
        "name": "unmute",
        "do": unmute
    }
]
