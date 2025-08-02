import os
import logging
import discord

from discord.ext import commands

from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger("bot")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='/d ', intents=intents)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
