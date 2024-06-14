import logging

logger = logging.getLogger('system_routes')
logger.setLevel(logging.WARNING)

fh = logging.FileHandler('system_routes.log')
fh.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
