import logging

# logging.basicConfig(level=logging.WARNING)

logger_person = logging.getLogger('person')
logger_person.setLevel(20)
# stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('person.log', 'a', encoding='utf-8')

log_format1 = logging.Formatter("%(asctime)s-%(name)s  \t\t-%(levelname)s\t\t\t\t-%(message)s")
# log_format_console1 = logging.Formatter("%(asctime)s \t -%(levelname)s \t -%(message)s")

# stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# stream_handler.setFormatter(log_format_console1)
file_handler.setFormatter(log_format1)

# logger_person.addHandler(stream_handler)
logger_person.addHandler(file_handler)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger_person.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logger_person.critical("Invalid age!")
        self._age = 0
