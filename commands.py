import asyncio
import inspect
import discord

from discord.ext import commands
from config import (
	logger,
	bot,
)
from utility import parse_time_string


class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Available commands",
            color=discord.Color.blue()
        )

        for cog, commands_list in mapping.items():
            filtered = await self.filter_commands(commands_list, sort=True)
            if not filtered:
                continue

            cog_name = cog.qualified_name if cog else "No Category"

            # Format command list: name + short description or 'No description'
            lines = []
            for cmd in filtered:
                short_desc = cmd.help.split('\n')[0] if cmd.help else "No description"
                padding = 12 - len(cmd.name)
                if padding < 0:
                    padding = 1  # prevent negative spaces if command is longer than 12 chars
                lines.append(f"`{cmd.name}` — {short_desc}")


            embed.add_field(name=cog_name, value="\n".join(lines), inline=False)

        embed.set_footer(
            text=(
                "Type `/d help` command for more info on a command.\n"
                "You can also type `/d help` category for more info on a category."
            )
        )

        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        help_text = command.help or inspect.getdoc(command.callback) or "No description given."

        embed = discord.Embed(
            title=f"Help for `{command.name}`",
            description=help_text,
            color=discord.Color.blue()
        )
        await self.get_destination().send(embed=embed)

bot.help_command = CustomHelp()


def setup():
    @bot.command(
        help=(
            "Sends the issuing user a notification.\n"
            "Usage:\n"
            "/d notify_me\n"
        )
    )
    async def notify_me(ctx):
        try:
            await ctx.author.send("You have been notified, my dude.")
            await ctx.send("Sent you a message, fucker!")

        except discord.Forbidden:
            logger.warning()
            await ctx.send("Your DMs are closed. If you wanna talk to me, open 'em first.")

        except Exception as e:
            await ctx.send(f"Unexpected error: {e}")


    @bot.command(
        help=(
            "Sends a predefined message to mentioned user.\n"
            "Usage:\n"
            "/d dm <@user>\n"
            "Arguments:\n"
            "username - Mentioned user, who you want to send a direct messege. \n"
        )
    )

    async def dm(ctx, member: discord.Member = None):
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


    @bot.command(
        help=(
            "Sets a timer for a specified duration.\n"
            "Usage:\n"
            "/d timer <time> <title>\n"
            "Arguments:\n"
            "time - Duration in seconds/minutes/hours/days. Examples: 10s, 5m, 2h, 1d.\n"
            "title - Optional title for the timer."
        )
    )
    async def timer(ctx, time: str, *, title: str = None):
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
