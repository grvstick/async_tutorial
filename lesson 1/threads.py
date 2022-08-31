from threading import Thread
from loguru import logger


def main_thread():
    sub_t = Thread(target=sub_thread)

    sub_t.start()
    for n in range(5):
        logger.info(n)

def sub_thread():
    for n in range(5):
        logger.info(n)


main_thread()