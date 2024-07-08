#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░▀█▀░█▀▄░█▀█░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▄█░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░░█░░█▀▄░█▀█░█░█░▀▀█░█▀▀░█░█░█▀▄░█░█░░░█░█░█░█░█░█░█░█░█░░░█▀▀
# ░░▀░░▀░▀░▀░▀░▀░▀░▀▀▀░▀░░░▀▀▀░▀░▀░▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀ © 2024 Pycon Mexico
# """
# @namespace scripts.transform
# Contains This module contains classes for transforming data.
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Mexico 2024 - CDMX

from libs import *
from utils import config_logging
from extract import Extract

sys.path.append(os.path.abspath('/Users/psf/Projects/pylab/charla-python-mexico/batch-release-etl'))
from config.settings import API_KEY, URL_API



class Transform:

    def __init__(self, data):
        self.data = data
        self.transformed_data = None

    def google_maps_api(self):
        self.data['lat'] = self.data['lat'].round(6)
        self.data['lon'] = self.data['lon'].round(6)
        dataset = []
        for lat, lon in zip(self.data['lat'], self.data['lon']):
            url = f"{URL_API}json?latlng={lat},{lon}&key={API_KEY}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    google_maps_address = response.json()
                    if google_maps_address['results']:
                        address_components = google_maps_address['results'][0]['address_components']
                        address = address_components[1].get('long_name', None) if len(address_components) > 1 else None
                        city = address_components[2].get('long_name', None) if len(address_components) > 2 else None
                        country = address_components[3].get('long_name', None) if len(address_components) > 3 else None
                        dataset.append([lat, lon, address, city, country])
                else:
                    print(f"API Error: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error making request: {e}")

        self.google_api_response = pd.DataFrame(dataset, columns=['lat', 'lon', 'address', 'city', 'country'])
        self.data = pd.merge(self.data, self.google_api_response, on=['lat', 'lon'], how='inner')
        logging.info("Google Maps API request successful.")

        return self.data


    def transform_data(self):
        try:
            self.data['weather_description'] = self.data['weather_description']
            self.data['name'] = self.data['name']
            self.data['lat'] = self.data['lat'].round(6)
            self.data['lon'] = self.data['lon'].round(6)
            self.data['sys_country'] = self.data['sys_country']
            self.data['match_address'] = self.data['name'] == self.data['address']
            self.data['match_city'] = self.data['name'] == self.data['city']
            self.data['match_country'] = self.data['name'] == self.data['country']

            self.data = self.data.drop_duplicates()
  
            self.transformed_data = self.data
            self.transformed_data.to_csv('data/transformed/openweathermap_transformed.csv', index=False)

            self.transformed_data = self.transformed_data[(self.transformed_data['match_address'] == True) | (self.transformed_data['match_city'] == True) | (self.transformed_data['match_country'] == True)]
            self.data = self.transformed_data.filter(['name', 'lat', 'lon', 'weather_description', 'sys_country', 'address', 'city', 'country'])

            logging.info("Data transformed successfully.")
        except Exception as e:
            raise Exception("log", e)

# if __name__ == '__main__':
#     config_logging()
#     extract = Extract()
#     extract.extract_data()
#     transform = Transform(extract.data)
#     transform.google_maps_api()
#     transform.transform_data()
#     print(transform.data.head())
