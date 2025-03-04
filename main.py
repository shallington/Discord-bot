import os
import discord
from discord.ext import commands
from discord.ui import Button, View

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online and ready!")

@bot.command()
async def verify(ctx):
    button = Button(label="✅ Verify Me!", style=discord.ButtonStyle.green, emoji="🔒")

    async def button_callback(interaction: discord.Interaction):
        role = discord.utils.get(ctx.guild.roles, name="Verified")  # Change this to your role name
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("🎉 **You're verified! Welcome!**", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ **The 'Verified' role does not exist!**", ephemeral=True)

    button.callback = button_callback
    view = View()
    view.add_item(button)

    embed = discord.Embed(
        title="🔒 Verification Required",
        description="Click the button below to verify and access the server!",
        color=discord.Color.green(),
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/847/847969.png")  # Custom Icon URL
    embed.set_footer(text="Verification System | Secure & Simple ✅")

    await ctx.send(embed=embed, view=view)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))