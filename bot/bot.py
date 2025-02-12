import telebot
from config.config import TELEGRAM_BOT_TOKEN
import logging
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def start_bot():
    logger.info("Бот запущен и ожидает сообщения...")
    while True:
        try:
            logger.info("Запуск polling...")
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            logger.error(f"Ошибка в работе бота: {e}")
            time.sleep(5)