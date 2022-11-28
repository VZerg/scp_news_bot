import logging
from telegram.ext import CommandHandler
from .controllers import Hellow
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
start_handler = CommandHandler('start', start)
# добавляем этот обработчик в `dispatcher`
dispatcher.add_handler(start_handler)