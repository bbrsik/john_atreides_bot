import discord
from config import (
	DISCORD_TOKEN, logger
)


intents = discord.Intents.default()
intents.message_content = True

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		logger.info(f"guild_name: {guild.name} - {guild.id=}")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	logger.info(f"John Atreides bot is in {guild_count} guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello John Atreides":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey stinky duner bitch")


bot.run(DISCORD_TOKEN)
