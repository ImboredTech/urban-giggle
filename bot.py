import discord
from discord.ext import commands
import config


bot = commands.Bot(command_prefix="!", owner_id=config.owner_id)



# Sets the bots status.
@bot.event
async def on_ready():
    print("Bot is online.")
    await bot.change_presence(activity=discord.Game(name="!help for commands."))



bot.run(config.token)