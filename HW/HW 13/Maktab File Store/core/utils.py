from os import name as os_name, system as terminal
import logging


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs.log')

log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# logger.addHandler(console_handler)
logger.addHandler(file_handler)
