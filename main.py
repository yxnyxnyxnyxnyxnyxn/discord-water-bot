import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from meme_generator import generate_meme

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANEL = os.getenv('CHANEL_ID')
bot = commands.Bot("!")


@tasks.loop(hours=1)
async def drink_water_reminder():
    message_channel = bot.get_channel(int(CHANEL))
    print(f"Got channel {message_channel}")
    url = generate_meme()
    print("meme url : ", url)
    embed = discord.Embed()
    embed.set_image(url=url)
    await message_channel.send(embed=embed)


@drink_water_reminder.before_loop
async def before():
    await bot.wait_until_ready()


drink_water_reminder.start()
bot.run(TOKEN)
