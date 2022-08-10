from time import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

st_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"process_timer.log")

st_format = logging.Formatter("%(asctime)s - %(name)8s - %(msg)8s ")

st_handler.setFormatter(st_format)
file_handler.setFormatter(st_format)

logger.addHandler(st_handler)
logger.addHandler(file_handler)


def process_timer(func):
    def wrapper(*args, **kwargs):
        t = time()
        res = func(*args, **kwargs)
        dt = time() - t
        if res > 100000:
            logger.info(f"<<{func.__name__}>> function - Finished: {dt:f} sec")
        return res
    return wrapper
