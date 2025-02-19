import discord
from discord.ext import commands, tasks
import asyncio
import os
from itertools import cycle
import keep_alive
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix="*", intents=discord.Intents.all())
bot_status = cycle(["/cat", "/dog", "/duck", "/fox"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    await client.tree.sync()
    print(f"Logged in as: {client.user}")
    guild_count = len(client.guilds)
    print(f"{client.user} connected to {guild_count} servers")
    change_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await client.load_extension(f"cogs.{filename[:-3]}")

keep_alive.keep_alive()

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())
