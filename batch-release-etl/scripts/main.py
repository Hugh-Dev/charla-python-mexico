#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░█▀█░█░█░█▀▀░█▀█░█▀█░░░
# ░█▀▀░░█░░█░░░█░█░█░█░░░
# ░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀░░░ MEXICO © 2024
# """
# @namespace scripts.main
# Contains 
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon México 2024 - CDMX


from libs import *
from extract import *
from transform import *
from load import *
from utils import *

@chronometer
def data_pipeline():
    
    try:
        print('Initializing data pipeline... 🐍​')
        config_logging()
        extract = Extract()
        extract.extract_data()
        transform = Transform(extract.data)
        transform.google_maps_api()
        transform.transform_data()
        load = Load(transform.data)
        load.load_data()
        print('Data pipeline executed successfully! 🚀')

    except Exception as e:
        raise Exception("log", e)


if __name__ == '__main__':
    try:
        data_pipeline()
    except Exception as e:
        print(f"An error occurred: {e}")