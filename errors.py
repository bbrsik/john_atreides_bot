import discord

from config import logger, bot
from discord.ext import commands


def setup():
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Nah I don't see them on this server, can't do that. Go fuck yourself.")
