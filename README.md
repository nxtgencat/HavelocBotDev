# Telegram Supabase Notifier

This is a Quart application that integrates with a Telegram bot and Supabase to send messages to users stored in a Supabase database.

## Features

- **Send Maintenance Messages**: Sends a predefined message to all users when the bot is in maintenance mode.
- **Send Custom Messages**: Allows sending a custom message to all users through a POST request.

## Prerequisites

- Python (>=3.7)
- Quart
- `supabase` Python library
- `python-telegram-bot` library
- `python-dotenv` library

You can install these dependencies using `pip`:

```bash
pip install quart supabase-python python-telegram-bot python-dotenv
