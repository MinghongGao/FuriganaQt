# set up logger
import logging.config
logging.config.fileConfig('logging.ini')
logger = logging.getLogger('root')
logger.debug("Set Up logger")
