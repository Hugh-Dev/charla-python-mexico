#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------#
# ░█▀█░▀█▀░█▀▄░░░▄▀▄░█░█░█▀█░█░░░▀█▀░▀█▀░█░█░░░█▀▀░█▀█░█▀█░█▀▀░█░░░█▀▀                       #
# ░█▀█░░█░░█▀▄░░░█\█░█░█░█▀█░█░░░░█░░░█░░░█░░░░█░█░█░█░█░█░█░█░█░░░█▀▀                       #
# ░▀░▀░▀▀▀░▀░▀░░░░▀\░▀▀▀░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀ © 2024 Python Mexico  #
# -------------------------------------------------------------------------------------------#
# @namespace scripts.air_quality_api
# Contains 
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon México 2024 - CDMX

from libs import *

sys.path.append(os.path.abspath('/Users/psf/Projects/pylab/charla-python-mexico/batch-release-etl'))
from config.settings import AIR_QUALITY_API


class AirQualityAPI:
    def __init__(self, data):
        self.data = data
        self.url = AIR_QUALITY_API

    def get_air_quality(self, latitude, longitude):
        payload = {
            "location": {
                "latitude": latitude,
                "longitude": longitude
            }
        }
        payload_json = json.dumps(payload)
        response = requests.post(self.url, data=payload_json, headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            data = response.json()
            indexes_data = data.pop('indexes')[0]
            return indexes_data.get('category', None)
        else:
            print("Error:", response.status_code)
            return None

    def update_data_with_categories(self):
        categories = []
        for _, row in self.data.iterrows():
            category = self.get_air_quality(row['lat'], row['lon'])
            categories.append(category)
        
        self.data['air quality'] = categories
        return self.data
    

# if __name__ == '__main__':
#     df = pd.DataFrame({
#     'latitude': [40.712776, 34.052235],
#     'longitude': [-74.005974, -118.243685]
#     })

#     api = AirQualityAPI(df)
#     df_updated = api.update_data_with_categories()
#     print(df_updated)