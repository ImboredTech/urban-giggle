import discord
from discord.ext import commands
import config
import os

bot = commands.Bot(command_prefix="!", owner_id=config.owner_id)



# Sets the bots status.
@bot.event
async def on_ready():
    print("Bot is online.")
    await bot.change_presence(activity=discord.Game(name="!help for commands."))


# Loads a cog.
@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 866285734808780812:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}.")
    else:
        await ctx.send("You do not have permission to use this command.")


# Unloads a cog.
@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 866285734808780812:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}.")
    else:
        await ctx.send("You do not have permission to use this command.")


# Reloads a cog
@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 866285734808780812:
        bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}.")
    else:
        await ctx.send("You do not have permission to use this command.")


# Loads all cogs on startup
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
    else:
        print(f"Failed to load {filename}")


bot.run(config.token)