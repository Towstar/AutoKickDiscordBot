# Discord AutoKick Bot

A Discord bot designed to automatically kick specified users from voice channels based on a predefined list. The bot includes commands to toggle the autokick feature and display the list of targeted users. Ideal for server moderators who need to enforce voice channel restrictions.

## Features

- **AutoKick**: Automatically disconnects users listed in `userKickList.txt` from voice channels when they join.
- **Toggle Command**: Enables or disables the autokick feature (restricted to users with the "Kick Commander" role).
- **Kick List Command**: Displays the list of users targeted for autokicking, including their display names and IDs.
- **Configurable Ban List**: User IDs are stored in a text file (`userKickList.txt`) for easy management.

## Prerequisites

- Python 3.8 or higher
- A Discord bot application with a valid token
- The "Kick Commander" role set up in your Discord server
- Necessary bot permissions: `Move Members`, `View Channels`, and `Send Messages`

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/discord-autokick-bot.git
   cd discord-autokick-bot
   ```

2. **Install Dependencies**
   Install the required Python packages using pip:

   ```bash
   pip install discord.py python-dotenv
   ```

3. **Configure Environment**

   - Create a `.env` file in the project root:
     ```env
     TOKEN=your_discord_bot_token
     ```
   - Replace `your_discord_bot_token` with your bot's token from the [Discord Developer Portal](https://discord.com/developers/applications).

4. **Prepare the Kick List**

   - Create a `userKickList.txt` file in the project root.
   - Add one Discord user ID per line. Example:
     ```
     1234567891011121314
     1234567891011121313
     ```

5. **Run the Bot**
   ```bash
   python bot.py
   ```

## Usage

- **Invite the Bot**: Add the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal. Ensure it has the required permissions.
- **Commands**:
  - `!toggle`: Toggles the autokick feature on or off (requires "Kick Commander" role).
    - Example: `!toggle` → "Autokick Activated ✅" or "Autokick Deactivated ❌"
  - `!kicklist`: Displays the list of users in `userKickList.txt` with their display names and IDs.
    - Example: `!kicklist` → "Kick list:\nUser1 (ID: 1234567891011121314)\nUser2 (ID: 1234567891011121313)"
- **Autokick Behavior**: When active, the bot automatically disconnects users from voice channels if their ID is in `userKickList.txt`.

## Project Structure

```
discord-autokick-bot/
├── bot.py              # Main bot script
├── userKickList.txt    # List of user IDs to autokick
├── .env                # Environment variables (not tracked in git)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Troubleshooting

- **Bot not responding**: Verify the bot token in `.env` is correct and the bot is online.
- **Users not kicked**: Ensure user IDs in `userKickList.txt` are valid and the bot has `Move Members` permission.
- **Command errors**: Confirm the "Kick Commander" role exists and is assigned to authorized users.
- **File errors**: Check that `userKickList.txt` is in the project root and contains valid user IDs (one per line).
