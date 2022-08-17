import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
	cogs[i].setup(client)

client.run("MTAwOTI0ODM3NTMyMjk3NjI1Ng.G108Id.yW5_dd82LgGNH-p24LjeYxd-u0XSJaiEUdcnss")
