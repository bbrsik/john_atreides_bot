import asyncio
import discord

from discord.ext.commands.errors import BadArgument

from config import (
	logger,
	bot,
)

from utility import parse_time_string


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


    @bot.command(help="Sets a timer for a specified duration.")
    async def timer(ctx, time: str, title=None):
        """
            Usage:
              !timer <time>

            Arguments:
              time - Duration in seconds/minutes/hours/days. Examples: 10s, 5m, 2h, 1d.
              title - A title for the timer. We surely need it.
        """
        seconds = parse_time_string(time)

        if seconds is None:
            await ctx.send("Bruh! Use format like `10s`, `5m`, `2h`, or `1d`. Otherwise I'm gonna fuck your dad.")
            return

        if title is None:
            await ctx.send("Ye about that... We'll need to set a `title` for the timer. Write it after the amount.")
            return

        if seconds > 60 * 60 * 24 * 30:
            await ctx.send("Timer too long. Keep it under 30 days, buddy.")
            return

        await ctx.send(f"Alright, timer titled `{title}` was just set for `{time}`!")

        await asyncio.sleep(seconds)

        await ctx.send(f"Atreides! {ctx.author.mention}, your `{time}` timer is up! It was titled as follows: `{title}`.")
