import requests
from pyfiglet import Figlet
import folium
from collections import defaultdict
import datetime
from pathlib import Path
import os 
import shutil

def save_location_to_map(response):
    dt = datetime.datetime.now()
    cur_time = dt.time().strftime("%H:%M:%S")
    try:
        area = folium.Map(location=[response.get('lat'), response.get('lon')],zoom_start=8)
        marker = folium.Marker(location=[response.get('lat'), response.get('lon')],popup=response.get('org'),icon=folium.Icon(color='red')).add_to(area)
        saved_map = area.save(f'{response.get("city")}_{cur_time}.html')
        cwd = os.getcwd
        
    except ValueError as e :
        print(e)
        print("try again ")
    

def get_info_by_ip(ip:str):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()        
        data = {
            'IP': response.get('query'),
            'Int prov': response.get('isp'),
            'Org': response.get('org'),
            'Country': response.get('country'),
            'Region Name': response.get('regionName'),
            'City': response.get('city'),
            'ZIP': response.get('zip'),
            'Lat': response.get('lat'),
            'Lon': response.get('lon'),
        }
        data = defaultdict(str)

        for k, v in data.items():
            print(f'{k} : {v}')
        save_location_to_map(response)
        print("your results are ready")
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
        
        
def main():
    preview_text = Figlet(font='moscow')
    print(preview_text.renderText('ipnator'))
    ip = input('enter ip : ')
    get_info_by_ip(ip=ip.strip())


if __name__ == '__main__':
    main()