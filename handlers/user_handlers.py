from bot import bot

def register_user_handlers(bot):
    @bot.message_handler(commands=["start"])
    def start_handler(message):
        bot.send_message(
            chat_id=message.chat.id,
            text="Привет"
        )