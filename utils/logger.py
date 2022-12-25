import logging
import sys


def log(msg, level='info'):
    raise Exception('deprecated since Report Portal logger is now used')
    # logger = logging.getLogger()
    # # logger.setLevel(logging.DEBUG)
    # # handler = logging.StreamHandler(sys.stdout)
    # # handler.setLevel(logging.DEBUG)
    # # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # # handler.setFormatter(formatter)
    # # logger.addHandler(handler)
    # logger.info(msg)
