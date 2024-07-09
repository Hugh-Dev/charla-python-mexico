#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------------------#
# ░█▀▀░█▀▀░█▀█░▀█▀░█░█░█▀▄░█▀▀░░░█▀▀░█▀█░█▀▀░▀█▀░█▀█░█▀▀░█▀▀░█▀▄░▀█▀░█▀█░█▀▀                      #
# ░█▀▀░█▀▀░█▀█░░█░░█░█░█▀▄░█▀▀░░░█▀▀░█░█░█░█░░█░░█░█░█▀▀░█▀▀░█▀▄░░█░░█░█░█░█                      #   
# ░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀ © 2024 Python Mexico #
# ------------------------------------------------------------------------------------------------#
# @namespace scripts.feature_engineering
# Contains 
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon México 2024 - CDMX

from libs import *

class FeatureEngineering:

    def __init__(self, data):
        self.data = data
        self.feature_engineering_data = None

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371 
        dlat = np.radians(lat2 - lat1)
        dlon = np.radians(lon2 - lon1)
        a = np.sin(dlat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        return R * c
    
    def feature_engineering(self):
        data = self.data.copy()
        cdmx_lat, cdmx_lon = 19.426949760876905, -99.16778174285928

        data['distance_to_cdmx'] = data.apply(lambda row: FeatureEngineering.haversine(row['lat'], row['lon'], cdmx_lat, cdmx_lon), axis=1)

        flight_speed_kmh = 800  
        car_speed_kmh = 100     

        data['flight_hours'] = data['distance_to_cdmx'] / flight_speed_kmh
        data['car_hours'] = data['distance_to_cdmx'] / car_speed_kmh

        data['distance_to_cdmx'] = data['distance_to_cdmx'].round(1)
        data['flight_hours'] = data['flight_hours'].round(2)
        data['car_hours'] = data['car_hours'].round(2)
        data['flight_minutes'] = (data['flight_hours'] * 60).astype(int)
        data['car_minutes'] = (data['car_hours'] * 60).astype(int)

        self.feature_engineering_data = data


# if __name__ == '__main__':
#     print('Initializing feature engineering... 🐍​')
#     print('\n')
#     data = pd.read_csv('./data/processed/openweathermap_processed.csv')
#     feature_engineering = FeatureEngineering(data)
#     feature_engineering.feature_engineering()
#     feature_engineering_data = feature_engineering.feature_engineering_data
#     print(feature_engineering_data.head())
#     print(feature_engineering_data.columns)
#     print('\n')
#     print('Feature engineering executed successfully! 🚀')

