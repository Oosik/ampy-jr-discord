import discord
import bot_commands as cmd
from discord.ext import commands
from utils import ImageUI
from config.settings import get_token, get_guild_id


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.tree.command(name="apy", description="Displays the 7D and 30D APYs for all Flexa collateral pools", guild=discord.Object(id=get_guild_id()))
async def apy(interaction: discord.Interaction):
    """
    Grabs the 7D and 30D APYs for all flexa collateral pools and sends them in a formatted string.

    Returns:
        str: A formatted string containing a table of the pools and their respective APYs.
    """
    await interaction.response.defer()
    table = cmd.apy()
    view = ImageUI(the_command="apy")
    await interaction.followup.send(f"```\n{table}```", view=view)

@bot.tree.command(name="price", description="Displays price and volume metrics", guild=discord.Object(id=get_guild_id()))
async def price(interaction: discord.Interaction):
    """
    Retrieves price and volume metrics and sends them in a formatted string.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that triggered this function.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    table = cmd.price('amp-token')
    view = ImageUI(the_command="price")
    await interaction.followup.send(f"```\n{table}```", view=view)


@bot.tree.command(name="tvl", description="Displays Flexa v3 pool TVL", guild=discord.Object(id=get_guild_id()))
async def tvl(interaction: discord.Interaction):
    """
    Retrieves the total value locked in all Flexa v3 pools and sends it in a formatted string.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that triggered this function.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    table = cmd.tvl()
    view = ImageUI(the_command="tvl")
    await interaction.followup.send(f"```\n{table}```", view=view)
    

@bot.tree.command(name="mc", description="Displays market cap metrics", guild=discord.Object(id=get_guild_id()))
async def mc(interaction: discord.Interaction):
    """
    Retrieves market cap metrics and sends them in a formatted string.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that triggered this function.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    table = cmd.mc('amp-token')
    view = ImageUI(the_command="mc")
    await interaction.followup.send(f"```\n{table}```", view=view)
    


@bot.tree.command(name="links", description="Displays useful community links", guild=discord.Object(id=get_guild_id()))
async def links(interaction: discord.Interaction):
    """
    Sends useful community links to the chat.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that triggered this function.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    text = cmd.links()
    await interaction.followup.send(f"{text}")




@bot.event
async def on_ready():
    print("------")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    for guild in bot.guilds:
        print(f"Connected to guild: {guild.name} (ID: {guild.id})")
    print("------")
    try:
        guild = discord.Object(id=get_guild_id())
        # bot.tree.clear_commands(guild=guild)
        sync = await bot.tree.sync(guild=guild)

        print(f"Synced {len(sync)} commands to guild {get_guild_id()}.")
        
        for command in bot.tree.get_commands(guild=guild):
            print(f"Registered: /{command.name}")
            
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    
    print("------")

    
if __name__ == '__main__':
    bot.run(get_token())
    