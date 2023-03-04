import discord
import random
from discord.ext import commands
from discord import Guild, app_commands

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1078537930458533970))
        self.synved = True
        print(">>Bot is online<<")

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="ping",description="Pings the user",guild=discord.Object(id=1078537930458533970))
async def self(interation: discord.Interaction, question:str):
    await interation.response.send_message(f"Pong")

@tree.command(name="eightball",description="gives you a answer",guild=discord.Object(id=1078537930458533970))
async def self(interation:discord.Interaction,question:str):
    responses = ["It is certain","Reply hazy,try again","Don’t count on it"]
    await interation.response.send_message(f"## Quesion:  {question}\n## Answers: {random.choice(responses)}")

bot.run("MTA4MDc5MTAzOTkyNjg3MDA0Ng.GJQTTD.WCSepYmE1Y0e1qw1NbOeAvk-5m9t7dx9e_vlWk")


