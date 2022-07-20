from person import Person
import logging

logging.basicConfig()
logger = logging.getLogger()

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('sample.log', 'a', encoding='utf-8')

log_format = logging.Formatter("%(asctime)s-%(name)s\t\t-%(levelname)s\t\t\t-%(msecs)s-%(message)s")
# log_format_console = logging.Formatter("%(asctime)s \t -%(levelname)s \t -%(message)s")

stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.ERROR)
# stream_handler.setFormatter(log_format_console)
file_handler.setFormatter(log_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def sub(a, b):
    if b != 0:
        logging.debug("a/b=" + str(a / b))
        return a / b
    logging.error("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
