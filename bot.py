import os, discord, random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([f"{member.name} - {member.id}" for member in guild.members])
    print(f'Guild Members:\n - {members}')
    print(f'{client.user.name} sono tornato merdeh!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Salve {member.name}, finalmente un nuovo amico con cui giocare!'
    )

@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    old_channel = member.voice.channel
    afk_channel = member.guild.afk_channel

    if member.id == 238681944873893889 and member.voice.self_stream == True and member.voice.channel != afk_channel:
        old_channel = member.voice.channel
        await member.move_to(afk_channel)
        await member.create_dm()
        await member.dm_channel.send("La smetti?!")
        await member.move_to(old_channel)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
client.run(TOKEN)
