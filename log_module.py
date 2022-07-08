"""
This log code demonstration is written by Shashidhar Reddy.
"""

# importing the libraries
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler


def initialise_logger(filepath, name):
    logger = logging.getLogger(name)
    handler = TimedRotatingFileHandler(filename=filepath, when='midnight', backupCount=15)
    current_time = int(time.time())

    rollover_time = handler.computeRollover(current_time)
    print(rollover_time)
    print('next log rotation: {}'.format(datetime.datetime.fromtimestamp(rollover_time)))

    formatter = logging.Formatter('%(asctime)s.%(msecs)03d: %(name)s - %(levelname)s - %(message)s',
                                  '%Y-%m-%dT%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    from random import randint
    import time
    lgr = initialise_logger('hello_log_test.log', __name__)

    for i in range(100):
        d = randint(1,500)
        if d % 3 == 0:
            lgr.info("Hey welcome to the file")
        elif d%4 == 0:
            lgr.error("Error in the file")
        elif d%5 == 0:
            lgr.warning("Warning message")
        else:
            lgr.debug("Debug message")
        e = randint(1,2)//2
        time.sleep(e)
