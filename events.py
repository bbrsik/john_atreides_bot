import discord

from config import (
	logger,
	bot,
)


def setup(bot):
	@bot.event
	async def on_ready():
		guild_count = 0

		for guild in bot.guilds:
			logger.info(f"guild_name: {guild.name} - {guild.id=}")
			guild_count = guild_count + 1

		logger.info(f"John Atreides bot is in {guild_count} guilds.")


	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			return

		if 'atreides' in message.content.lower():
			await message.channel.send("Atreides!")

		await bot.process_commands(message)