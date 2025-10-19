import discord
from discord.ext import commands
from datetime import datetime
import os
import pytz
import json

# Load the bot token from an environment variable
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# --- Timezone and Menu Data ---
IST = pytz.timezone('Asia/Kolkata')

def load_menu_data(file_path):
    """Loads menu data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The menu data file was not found at {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode the JSON from {file_path}")
        return {}

MENU_DATA = load_menu_data('menu_data.json') # This will now load the external menu data

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('Bot is now online and ready to serve menus!')
    print('------')


@bot.command(name='menu')
async def send_menu(ctx):
    now_ist = datetime.now(IST)
    current_hour = now_ist.hour
    current_date_str = now_ist.strftime("%d-%m-%Y")
    daily_menu = MENU_DATA.get(current_date_str) if MENU_DATA else None
    
    if not daily_menu:
        embed = discord.Embed(
            title="No Menu Available Today 😕",
            description=f"Sorry, I couldn't find a menu for {now_ist.strftime('%A, %d %B %Y')}.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    menu_title = ""
    meal_items = []
    
    if 5 <= current_hour < 9:
        menu_title = f"Breakfast Menu 🍳 - {now_ist.strftime('%A')}"
        meal_items = daily_menu.get("Breakfast", [])
    elif 9 <= current_hour < 14:
        menu_title = f"Lunch Menu 🍛 - {now_ist.strftime('%A')}"
        meal_items = daily_menu.get("Lunch", [])
    elif 14 <= current_hour < 17:
        menu_title = f"Evening Snacks Menu ☕️ - {now_ist.strftime('%A')}"
        meal_items = daily_menu.get("Snacks", [])
    elif 17 <= current_hour < 21:
        menu_title = f"Dinner Menu 🍽️ - {now_ist.strftime('%A')}"
        meal_items = daily_menu.get("Dinner", [])
    else:
        menu_title = "The Kitchen is Closed! 🌙"
        meal_items = ["Please come back during our regular meal times."]

    menu_description = "\n".join(f"• {item}" for item in meal_items) if meal_items else "Menu not available for this meal."

    embed = discord.Embed(
        title=menu_title, 
        description=menu_description, 
        color=discord.Color.gold()
    )
    embed.set_footer(text=f"Date: {now_ist.strftime('%d %B %Y')} | Time: {now_ist.strftime('%I:%M %p %Z')}")
    await ctx.send(embed=embed)


if __name__ == "__main__":
    if not BOT_TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable not found. Exiting.")
        print("Please set the token in your environment or a .env file.")
        exit()

    try:
        bot.run(BOT_TOKEN)
    except discord.errors.LoginFailure:
        print("Login failed. Please check that your DISCORD_BOT_TOKEN is correct and valid.")
    except Exception as e:
        print(f"An error occurred: {e}")
