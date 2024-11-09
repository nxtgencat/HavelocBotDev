import os

import supabase
import telegram
from dotenv import load_dotenv
from quart import Quart, request
from supabase import create_client

# Load environment variables from .env file
load_dotenv()

# Get the bot token and Supabase URL/API key from environment variables
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase_client = create_client(supabase_url, supabase_key)

app = Quart(__name__)

bot = telegram.Bot(token=bot_token)


@app.route('/maintenance', methods=['GET'])
async def send_test_messages():
    # Fetch all users from the users table
    users = supabase_client.table("users").select("chat_id").execute()

    # Send a message to each chat_id
    for user in users.data:
        chat_id = user['chat_id']
        await bot.send_message(chat_id=chat_id,
                               text="We are working hard on new features! The bot is in development mode. Thanks for your patience.")

    return "Messages sent!"


# New Route for Sending Custom Message
@app.route('/notify', methods=['POST'])
async def send_custom_message():
    # Get the custom message from the request body
    data = await request.json
    custom_message = data.get("message", "")

    if not custom_message:
        return {"error": "No message provided"}, 400

    # Fetch all users from the users table
    users = supabase_client.table("users").select("chat_id").execute()

    # Send the custom message to each chat_id
    for user in users.data:
        chat_id = user['chat_id']
        await bot.send_message(chat_id=chat_id, text=custom_message)

    return {"status": "Custom messages sent!"}


if __name__ == '__main__':
    app.run(port=5000)
