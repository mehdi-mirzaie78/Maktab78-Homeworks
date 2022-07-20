import logging

# logging.basicConfig(level=logging.WARNING)
logging.basicConfig()
logger = logging.getLogger()

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('person.log', 'a', encoding='utf-8')

log_format = logging.Formatter("%(asctime)s-%(name)s  \t\t-%(levelname)s\t\t\t\t-%(message)s")
log_format_console = logging.Formatter("%(asctime)s \t -%(levelname)s \t -%(message)s")

stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(log_format_console)
file_handler.setFormatter(log_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logging.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.critical("Invalid age!")
        self._age = 0
