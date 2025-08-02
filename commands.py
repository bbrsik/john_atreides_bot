import asyncio
import discord

from discord.ext.commands.errors import BadArgument

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
            await ctx.send("Your DMs are closed. If you wanna talk to me, open 'em first.")

        except Exception as e:
            await ctx.send(f"Unexpected error: {e}")


    @bot.command()
    # todo doesn't really work, figure out later
    async def dm(ctx, member: discord.Member=None):
        if member is None:
            await ctx.send("Who do you expect me to DM? Your mom? Tag someone right after the command!")

        try:
            await member.send('sup fool')
            await ctx.send(f"Ye I got that {member.display_name} dude a message.")

        except discord.Forbidden as e:
            await ctx.send("They have their DMs disabled. The fuck?")
            logger.warning(f"Exception: {e}")

        except Exception as e:
            await ctx.send(f"Unexpected error: {e}")
