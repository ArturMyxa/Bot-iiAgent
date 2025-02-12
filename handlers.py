from telebot import types
from bot.bot import bot
from data.product_matrix import get_product_data, save_contact_info
import logging

logger = logging.getLogger(__name__)
user_data = {}

# ... (остальные функции остаются без изменений)

@bot.message_handler(func=lambda message: message.text.lower() in ["ремонт", "новое"])
def handle_choice(message):
    engine_brand = user_data[message.chat.id]["engine_brand"]
    if message.text.lower() == "ремонт":
        handle_repair(message, engine_brand)
    else:
        handle_replacement(message, engine_brand)

@bot.message_handler(func=lambda message: message.text.lower() == "назад")
def handle_back(message):
    user_data[message.chat.id]["engine_brand"] = None
    bot.send_message(message.chat.id, "Напишите марку вашего двигателя:")

def save_phone_number(message):
    phone_number = message.text
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(types.KeyboardButton('Отправить'), types.KeyboardButton('Назад'))
    bot.send_message(
        message.chat.id,
        f"Ваш номер: {phone_number}. Подтвердите отправку:",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, confirm_send)

def confirm_send(message):
    if message.text.lower() == "отправить":
        try:
            save_contact_info(
                chat_id=message.chat.id,
                engine_brand=user_data[message.chat.id]["engine_brand"],
                phone_number=user_data[message.chat.id].get("phone")
            )
            bot.send_message(message.chat.id, "✅ Номер сохранен в таблицу.")
        except Exception as e:
            logger.error(f"Ошибка при сохранении номера: {e}")
            bot.send_message(message.chat.id, "❌ Ошибка сохранения.")
    elif message.text.lower() == "назад":
        handle_back(message)
    else:
        bot.send_message(message.chat.id, "Действие отменено.")