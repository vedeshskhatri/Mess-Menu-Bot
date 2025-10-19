# Cafeteria Menu Discord Bot

This is a simple Discord bot that provides the daily cafeteria menu based on the current time in India (IST). It fetches menu data for Breakfast, Lunch, Evening Snacks, and Dinner.

## Features

- Displays the menu for the current mealtime (Breakfast, Lunch, Snacks, Dinner).
- Uses Indian Standard Time (IST) for time-based menu retrieval.
- Provides a clear and formatted output using Discord embeds.
- Easily extensible menu data for future dates.

## Setup Instructions

### 1. Prerequisites

- Python 3.8+
- A Discord Bot Token (get one from the [Discord Developer Portal](https://discord.com/developers/applications))

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Bot Token

**IMPORTANT:** Do NOT hardcode your bot token directly into the `Mess.py` file. Instead, set it as an environment variable.

- **Linux/macOS:**
  ```bash
  export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
  ```
- **Windows (Command Prompt):**
  ```cmd
  set DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
  ```

Replace `"YOUR_BOT_TOKEN_HERE"` with the actual token you obtained from the Discord Developer Portal.

### 4. Run the Bot

Navigate to the directory where `Mess.py` is located in your terminal and run:

```bash
python Mess.py
```

The bot should log in and print a confirmation message to your console.

### 5. Invite the Bot to Your Discord Server

You'll need to invite your bot to your Discord server. You can generate an invite link from the Discord Developer Portal under your application's "OAuth2" -> "URL Generator" section. Make sure to grant it the necessary permissions (e.g., "Send Messages", "Embed Links").

## Usage

Once the bot is running and in your server, simply type the following command in any channel the bot can see:

```
-menu
```

The bot will respond with the current meal's menu.

## Extending the Menu

The `menu_data.json` file holds all the menu information. You can extend this file with more dates and meal items. The keys for the dates should be in `DD-MM-YYYY` format.