import json
import requests

from analyzers.continent_analyzer import ContinentDictAnalyzer
from db.dal_queries.tables import Tables
from db.db_handler import DbHandler
from readers.json_reader import JsonReader

# url = 'https://parseapi.back4app.com/classes/Country?limit=350&include=continent&keys=name,continent,continent.name'
# headers = {
#     'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',  # This is the fake app's application id
#     'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'  # This is the fake app's readonly master key
# }
# data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
# path = f'dataset/continent.json'
# print(f"creating {path}")
# with open(path, 'w') as f:
#     json.dump(data, f, indent=2)
db_handler = DbHandler()
analyzers = [ContinentDictAnalyzer(db_handler)]
json_reader = JsonReader()
data = json_reader.read_file(f'dataset/continent.json')
for raw_data in data['results']:
    for analyzer in analyzers:
        analyzer.analyze_dict(raw_data)
db_handler.flush_to_db(Tables.COUNTRIES_TABLE)
