def save_chat_history(user_message, bot_response):
    chat_collection.insert_one({"user": user_message, "bot": bot_response})
