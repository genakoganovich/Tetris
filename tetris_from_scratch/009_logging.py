import logging

logging.basicConfig(level=logging.DEBUG,
                    format = "line %(lineno)d: %(message)s")
logging.debug("A new debug message")