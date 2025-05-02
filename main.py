from discord.ext import commands
import discord
import os
from dotenv import load_dotenv


USER_BAN_LIST = []
try:
    with open('userKickList.txt') as list_file:
        for user_id in list_file:
            user_id = user_id.strip()
            if user_id:
                try:
                    USER_BAN_LIST.append(user_id)
                except ValueError:
                    print(f"Invalid user ID in userKickList.txt: {user_id}")
except FileNotFoundError:
    print("userKickList.txt not found. Starting with empty ban list.")
except Exception as e:
    print(f"Error reading userKickList.txt: {e}")

active = True

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    
@bot.command()
@commands.has_role("Kick Commander")
async def toggle(ctx):
    global active
    active = not active
    status = "Activated ✅" if active else "Deactivated ❌"
    await ctx.send(f"Autokick {status}")

    
@bot.command()
async def kicklist(ctx):
    if not USER_BAN_LIST:
        await ctx.send("Kick list is empty.")
        return

    guild = ctx.guild
    user_info = []

    for user_id in USER_BAN_LIST:
        try:
            member = await guild.fetch_member(user_id)
            display_name = member.nick if member.nick else member.global_name or member.name
            user_info.append(f"{display_name} (ID: {user_id})")
        except discord.NotFound:
            user_info.append(f"User not found (ID: {user_id})")
        except discord.HTTPException as e:
            user_info.append(f"Error fetching user (ID: {user_id}): {e}")

    await ctx.send(f"Kick list:\n" + "\n".join(user_info))
    
@bot.event
async def on_voice_state_update(member, before, after):
    if ((member.id in USER_BAN_LIST) and (after.channel is not None) and (active is True)):
        try:
            await member.move_to(None)
            print(f"🥾 Kicked {member} from voice channel {after.channel.name}.")
        except Exception as e:
            print(f"💔 Failed to kick {member}: {e}")
        
bot.run(TOKEN)