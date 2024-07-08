#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░█░░░█▀█░█▀█░█▀▄░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░█░░░█░█░█▀█░█░█░░░█░█░█░█░█░█░█░█░█░░░█▀▀
# ░▀▀▀░▀▀▀░▀░▀░▀▀░░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀ © 2024 Pycon Mexico
# """
# @namespace scripts.load
# Contains .
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Mexico 2024 - CDMX

from libs import *
from utils import config_logging

class Load:
    
    def __init__(self, data):
        self.data = data
        self.path = './data/processed'
        self.file = 'openweathermap_processed.csv'
        self.listdir = os.listdir(self.path)

    def load_data(self):
        try:
            if self.file in self.listdir:
                self.data.to_csv(f'{self.path}/{self.file}', index=False)
                logging.info("Data loaded successfully.")
                
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS weather_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        lat FLOAT,
                        lon FLOAT,
                        weather_description TEXT,
                        sys_country TEXT,
                        address TEXT,
                        city TEXT,
                        country TEXT
                    )
                ''')
                
                self.data.to_sql('weather_data', conn, if_exists='append', index=False)
                conn.commit()
                conn.close()
                
            else:
                raise Exception("File not found...")
            
        except Exception as e:
            raise Exception("log", e)