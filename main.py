import discord
from discord.ext import commands

# Initialize intents ***************************************
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.presences = True
intents.members = True
intents.guild_messages = True

# Initialize the bot instance ***************************************
bot = commands.Bot(command_prefix="orga ", intents=intents)

@bot.tree.command(name="test", description="test command")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Testing...", ephemeral=True)


# bot event ***************************************
# On ready ------------------------------------------------
@bot.event
async def on_ready():
    print('Ready!')
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"ActiveDevBadge")
    await bot.change_presence(status=discord.Status.online, activity=activity)

    await bot.tree.sync()


# connect using token ***************************************
# ------------------------------------------------
Secret = open("secret.txt", 'r')
Secret = Secret.read()

bot.run(Secret)