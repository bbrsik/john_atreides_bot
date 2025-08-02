import discord

from config import (
	logger,
	bot,
)


def setup():
    @bot.command()
    async def notify_me(ctx):
        try:
            await ctx.author.send("You have been notified, my dude.")
            await ctx.send("Sent you a message, fucker!")
        except discord.Forbidden:
            logger.warning()
            await ctx.send("Your DMs are closed. If you wanna talk to me, open 'em.")


    @bot.command()
    # todo doesn't really work, figure out later
    async def dm(ctx, member: discord.Member):
        try:
            await member.send('sup fool')
            await ctx.send(f"Ye I got that {member.display_name} dude.")
        except discord.Forbidden:
            await ctx.send("This guy has DMs disabled. The fuck?")
