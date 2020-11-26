import json
import requests

from analyzers.capital_dict_analyzer import CapitalDictAnalyzer
from analyzers.city_dict_analyzer import CityDictAnalyzer
from db.db_handler import DbHandler

url = 'https://parseapi.back4app.com/classes/City?limit=11&include=country&keys=name,country,country.name,country.capital,population,location'
headers = {
    'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',  # This is the fake app's application id
    'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'  # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need

db_handler = DbHandler()
analyzers = [CityDictAnalyzer(db_handler), CapitalDictAnalyzer(db_handler)]
for raw_data in data['results']:
    for analyzer in analyzers:
        analyzer.analyze_dict(raw_data)

# db_handler.flush_to_db(Tables.COUNTRIES_TABLE)
