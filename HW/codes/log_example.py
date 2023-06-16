import logging

def get_logger(name, path, base_level=logging.DEBUG, log_format=None):
    if log_format is None:
        log_format = "%(asctime)s -\t %(name)s - %(levelname)s\t - %(message)s"
    logger = logging.getLogger(name)
    logger.setLevel(base_level)

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(path)
    
    stream_handler.setFormatter(log_format)
    file_handler.setFormatter(log_format)

    stream_handler.setLevel(base_level)
    file_handler.setLevel(base_level)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger

