import json
import os

import requests

from analyzers.capital_dict_analyzer import CapitalDictAnalyzer
from analyzers.city_dict_analyzer import CityDictAnalyzer
from db.dal_queries.tables import Tables
from db.db_handler import DbHandler
from readers.json_reader import JsonReader

# skip = 0
# limit = 2500
# total = 0
#
# db_handler = DbHandler()
# analyzers = [CityDictAnalyzer(db_handler)]
#
# while total < 1362963:
#
#     url = f'https://parseapi.back4app.com/classes/City?skip={skip}&limit={limit}&include=country&keys=name,country,country.name,country.capital,population,location'
#     headers = {
#         'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',  # This is the fake app's application id
#         'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'  # This is the fake app's readonly master key
#     }
#     data = json.loads(
#         requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
#
#     total = total + len(data['results'])
#     skip = skip + limit
#
#     for raw_data in data['results']:
#         for analyzer in analyzers:
#             analyzer.analyze_dict(raw_data)
#
#     path = f'dataset/cities/cities{skip}.json'
#     print(f"creating {path}")
#     with open(path, 'w') as f:
#         json.dump(data, f, indent=2)
#
# db_handler.flush_to_db(Tables.CITY_TABLE)


# read from file instead of re-download everything #

path_to_json = os.path.join("dataset", "cities")
json_files = [os.path.join(path_to_json, pos_json) for pos_json in os.listdir(path_to_json) if
              pos_json.endswith('.json')]

db_handler = DbHandler()
json_reader = JsonReader()
# analyzers = [CityDictAnalyzer(db_handler)]
analyzers = [CapitalDictAnalyzer(db_handler)]

for file in json_files:
    data = json_reader.read_file(file)
    for raw_data in data['results']:
        for analyzer in analyzers:
            analyzer.analyze_dict(raw_data)

# db_handler.flush_to_db(Tables.CITY_TABLE)
db_handler.flush_to_db(Tables.CAPITAL_TABLE)
