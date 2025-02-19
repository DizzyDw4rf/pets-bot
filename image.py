import discord
from discord import app_commands
from discord.ext import commands
import requests
import aiohttp
import json
from datetime import datetime


class Image(commands.Cog):
    
    date = datetime.now()
    
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="cat", description="shows a random Cat Image.")
    @app_commands.checks.cooldown(1, 5, key = lambda i : (i.user.id))
    async def cat(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as r:
                raw = await r.text()
                cat = json.loads(raw)[0]
                cat_embed = discord.Embed(title="Meow", color=discord.Colour.random())
                cat_embed.set_image(url=cat["url"])
                cat_embed.set_footer(text=f"Powerd by TheCatAPI")
                await interaction.response.send_message(embed=cat_embed)

    @app_commands.command(name="dog", description="shows a random Dog Image.")
    @app_commands.checks.cooldown(1, 5, key = lambda i : (i.user.id))
    async def dog(self, interaction: discord.Interaction):
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        res = r.json()
        dog_embed = discord.Embed(title="Woof", color=discord.Colour.random())
        dog_embed.set_image(url=res["message"])
        dog_embed.set_footer(text=f"Powered by Dog.Ceo")
        await interaction.response.send_message(embed=dog_embed)
    
    
    @app_commands.command(name="duck", description="shows a random Duck Image.")
    @app_commands.checks.cooldown(1, 5, key = lambda i : (i.user.id))
    async def duck(self, interaction: discord.Interaction):
        r = requests.get("https://random-d.uk/api/random")
        res = r.json()
        duck_embed = discord.Embed(title="Quack", color=discord.Colour.random())
        duck_embed.set_image(url=res["url"])
        duck_embed.set_footer(text=f"{res["message"]}")
        await interaction.response.send_message(embed=duck_embed)

    @app_commands.command(name="fox", description="shows a random Fox Image.")
    @app_commands.checks.cooldown(1, 5, key = lambda i : (i.user.id))
    async def fox(self, interaction: discord.Interaction):
        r = requests.get("https://randomfox.ca/floof")
        res = r.json()
        fox_embed = discord.Embed(title="Howl", color=discord.Colour.random())
        fox_embed.set_image(url=res["image"])
        fox_embed.set_footer(text=f"Powerd by RandomFox.ca")
        await interaction.response.send_message(embed=fox_embed)

async def setup(client):
    await client.add_cog(Image(client))
