import discord

import events
import commands

from config import (
	bot,
	DISCORD_TOKEN,
	logger
)

events.setup(bot)
commands.setup(bot)

bot.run(DISCORD_TOKEN)
