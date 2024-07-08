
#!/usr/bin/env python3
# -*- coding: utf-8 -*-# """
# ░█░█░▀█▀░▀█▀░█░░░▀█▀░▀█▀░▀█▀░█▀▀░█▀▀
# ░█░█░░█░░░█░░█░░░░█░░░█░░░█░░█▀▀░▀▀█
# ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀
# """
# @namespace scripts.utils
# Contains 
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon México 2024 - CDMX

from libs import *


def config_logging():
    path_logs = './logs'
    if not os.path.exists(path_logs):
        os.makedirs(path_logs)
    file = 'etl_process.log'
    logging.basicConfig(
        filename=os.path.join(path_logs, file),
        filemode='w', 
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def chronometer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"The function '{func.__name__}' took {total_time} seconds to execute. ⏳")
        return result
    return wrapper