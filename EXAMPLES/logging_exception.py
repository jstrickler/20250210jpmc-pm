
import logging

logging.basicConfig( # configure logging
    filename='../LOGS/exception.log',
    level=logging.WARNING,  # minimum level
)

for i in range(3):
    try:
        result = i/0
    except ZeroDivisionError as err:
        # print(dir(err))
        # print(err.with_traceback())
        logging.exception('Logging with exception info') # add exception info to the log
