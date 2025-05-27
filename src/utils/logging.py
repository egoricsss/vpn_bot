import glob
import logging
import os
import queue
from logging.handlers import QueueHandler, QueueListener

from src.core.config import config


def clear_logs_folder(log_dir="logs", pattern="bot.log*"):
    try:
        if os.path.exists(log_dir):
            log_files = glob.glob(os.path.join(log_dir, pattern))
            for f in log_files:
                os.remove(f)
                logging.info(f"🤗 Deleted file: {f}")
        else:
            logging.info(f"🐻 dir {log_dir} not found")
    except Exception as e:
        logging.info(f"❌ Error while deleting logs: {e}")

os.makedirs("logs", exist_ok=True)
log_queue = queue.Queue()

formatter = logging.Formatter(
    fmt='%(asctime)s [%(levelname)s] %(module)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger("TelegramBotLogger")
logger.setLevel(logging.DEBUG)

if config.CLEAR_LOGS:
    clear_logs_folder()

file_handler = logging.FileHandler('logs/bot.log')
file_handler.setFormatter(formatter)

queue_handler = QueueHandler(log_queue)
logger.addHandler(queue_handler)

queue_listener = QueueListener(log_queue, file_handler, console_handler, respect_handler_level=True)
queue_listener.start()

logger.debug("✅ Logging is ready for work")


def get_logger() -> logging.Logger:
    return logger
