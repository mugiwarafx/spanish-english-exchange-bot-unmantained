import os

from server.keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py") and filename != "__init__.py":
    bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))