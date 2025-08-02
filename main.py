import discord

import events
import commands
import errors  # hehe

from config import (
	bot,
	DISCORD_TOKEN,
	logger
)

events.setup()
commands.setup()
errors.setup()

bot.run(DISCORD_TOKEN)
