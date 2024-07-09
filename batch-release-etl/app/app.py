# --------------------------------------------------------#
# ░█▀█░█▀█░█▀█░░░█▀▀░█░░░█▀█░█▀▀░█░█                      #
# ░█▀█░█▀▀░█▀▀░░░█▀▀░█░░░█▀█░▀▀█░█▀▄                      #
# ░▀░▀░▀░░░▀░░░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀ © 2024 Python México #
# --------------------------------------------------------#
# @namespace app.app
# Contains .
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Mexico 2024 - CDMX


from flask import Flask, render_template_string
import folium
import branca
import pandas as pd
import sqlite3
import requests
import subprocess
import sys

app = Flask(__name__)

def pipeline():
    try:
        process_output = subprocess.run(["python", "scripts/main.py"], stdout=sys.stdout, stderr=sys.stderr)
        if process_output.returncode == 0:
            return True
    except Exception as e:
        print(f"Error running pipeline: {e}")
    


def get_random_location_data():

    with sqlite3.connect('database.db') as conn:
        query = "SELECT * FROM weather_data;"
        try:
            response = pd.read_sql_query(query, conn)
        except Exception as e:
            print(f"Error reading from database: {e}")
            return None
    
    return response.sample(n=1)

def create_map(random_row):

    lat = random_row['lat'].values[0]
    lon = random_row['lon'].values[0]


    html = f"""
    <table style="border-collapse: collapse; font-size: 12px; font-family: sans-serif; border-radius: 10px;>
        <tr>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;"></th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Latitude</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Longitude</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Weather Description</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">City</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Country</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Distance to CDMX (km)</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Flight Minutes</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Car Minutes</th>
            <th style="width: 12.5%; text-align: center; font-style: italic; padding: 10px;">Air Quality</th>
        </tr>
    """
    for index, row in random_row.iterrows():
        html += f"""
        <tr>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['lat']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['lon']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['weather_description']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['city']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['country']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['distance_to_cdmx']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['flight_minutes']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['car_minutes']}</td>
            <td style="border-top: 1px solid #dee2e6; background-color: rgba(0,0,0,.08); text-align: center; padding: 10px;">{row['air quality']}</td>
        </tr>
    """

    html += """
    </table>
    """

    iframe = branca.element.IFrame(html=html, width=900, height=150)
    popup = folium.Popup(iframe, max_width=900)

    m = folium.Map(location=(lat, lon), zoom_start=12)
    folium.Marker(
        location=[lat, lon],
        tooltip="Click me!",
        popup=popup,
        icon=folium.Icon(),
    ).add_to(m)

    return m._repr_html_()


@app.route('/')
def map():
    if pipeline():
        random_row = get_random_location_data()
        if random_row is None:
            return render_template_string("<h1>There was an error processing your request</h1>")
        
        map_html = create_map(random_row)
        return render_template_string(map_html)
    else:
        return render_template_string("<h1>There was an error processing your request</h1>")

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.57', port=5000)