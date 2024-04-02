# Discord Riddle Bot

This Discord bot provides users with riddles and allows them to guess the answers.

## features

- Riddle Command: Use !riddle command to get a random riddle.
- Answer Command: Use !answer command to get the answer to the last riddle.
- Multiple Channels Support: Keeps track of the last riddle asked in each channel separately.
- Interactive: Engage users with fun riddles and keep them entertained.


## Requirements

- Python 3.x
- Discord.py library('pip install discord.py)


1. Clone this repository:

     ```
    git clone https://github.com/theZoid9/discord-riddle-bot.git
    ```

2. Navigate to the project directory:
    
    ```
    cd discord-riddle-bot
    ```

3. Install dependencies:
    
    ```
    pip install -r requirements.txt
    ```

4. Obtain a Discord Bot Token:
 
 - Go to the Discord Developer Portal.
 - Create a new application.
 - Under the "Bot" tab, click "Add Bot "
 - Copy the ticket.

5. Configure the Bot:
 
 - Open "bot.py" in text editor.
 - Replace 'discord token with the one you obtain in step 4.

 6. Run the Bot:

    ```
    python bot.py
    ```

## Usage

- Once the bot is running and added to your Discord server, users can interact with it using the provided commands.
- Use !riddle to get a random riddle.
- Use !answer to get the answer to the last riddle asked in the current channel.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.