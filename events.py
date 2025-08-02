import discord

from config import (
	logger,
	bot,
)


def setup():
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

		message_content = message.content.lower()
		answer_amount = 0

		if 'atreides' in message_content:
			while 'atreides' in message_content:
				answer_amount += 1
				message_content = message_content.replace('atreides', '', 1)
			await message.channel.send("Atreides! " * answer_amount)

		await bot.process_commands(message)
