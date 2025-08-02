import discord

import events
import commands

from config import (
	bot,
	DISCORD_TOKEN,
	logger
)

events.setup()
commands.setup()

bot.run(DISCORD_TOKEN)
