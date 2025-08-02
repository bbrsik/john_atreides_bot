import discord

from config import logger, bot
from discord.ext import commands


def setup():
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Nah I don't see them on this server, can't do that. Go fuck yourself.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command `{ctx.invoked_with}` not found. Try `/d help` to find out what I do here.")
        else:
            logger.warning(f"Don't know how to handle this error:\n {error}")
