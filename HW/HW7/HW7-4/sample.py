from person import Person
import logging

logger_sample = logging.getLogger('sample')
logger_sample.setLevel(10)

stream_handler2 = logging.StreamHandler()
file_handler2 = logging.FileHandler('sample.log', 'a', encoding='utf-8')

log_format = logging.Formatter("%(asctime)s-%(name)s\t\t-%(levelname)s\t\t\t-%(msecs)s-%(message)s")
log_format_console = logging.Formatter("%(asctime)s \t -%(levelname)s \t -%(message)s")

stream_handler2.setLevel(logging.INFO)
file_handler2.setLevel(logging.ERROR)
stream_handler2.setFormatter(log_format_console)
file_handler2.setFormatter(log_format)

logger_sample.addHandler(stream_handler2)
logger_sample.addHandler(file_handler2)


def sub(a, b):
    if b != 0:
        logger_sample.debug("a/b=" + str(a / b))
        return a / b
    logger_sample.error("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
