#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░█▀▀░█░█░▀█▀░█▀▄░█▀█░█▀▀░▀█▀░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░█▀▀░▄▀▄░░█░░█▀▄░█▀█░█░░░░█░░░░█░█░█░█░█░█░█░█░█░░░█▀▀
# ░▀▀▀░▀░▀░░▀░░▀░▀░▀░▀░▀▀▀░░▀░░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀  ©2024 Pycon Mexico
# """
# @namespace scripts.extract
# Contains .
# @author Hugo Ramirez (@hughpythoneer as X)
# Pycon Mexico 2024 - CDMX

from libs import *
from utils import config_logging


class Extract:

    def __init__(self):
        self.data = None
        self.path = './data/raw'
        self.file = 'openweathermap_raw.csv'
        self.listdir = os.listdir(self.path)

    def extract_data(self):
        try:
            if self.file in self.listdir:
                self.data = pd.read_csv(f'{self.path}/{self.file}')
                logging.info("Data extracted successfully.")
            else:
                raise Exception("File not found...")
            
        except Exception as e:
            raise Exception("log", e)
        

# if __name__ == '__main__':
#     config_logging()
#     extract = Extract()
#     extract.extract_data()
#     print(extract.data.head())
#     print(extract.data.info())
#     print(extract.data.describe())
#     print(extract.data.columns)
#     print(extract.data.shape)
#     print(extract.data.dtypes)

