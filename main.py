from flask import Flask  
from threading import Thread  

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Start the Flask web server in a separate thread
Thread(target=run).start()
import discord
import os
import logging
from discord.ext import commands

# Disable discord.py's INFO logs
discord.utils.setup_logging(level=logging.WARNING)

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))