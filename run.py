import discord
intents = discord.Intents.default()
intents.all = True
client = discord.Client(intents=intents)