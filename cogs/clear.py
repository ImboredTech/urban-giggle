import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title="Cleared Messages", description=f"{amount} messages have been cleared.", color=0x00ff00)
        await ctx.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(Clear(bot))