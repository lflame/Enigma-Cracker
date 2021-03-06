import logging

logger = logging.getLogger()
fh = logging.FileHandler('log.txt', encoding='utf-8')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)
