import os

from analyzers.ethincs_analyzer import EthnicsDictAnalyzer
from db.dal_quries.tables import Tables
from db.db_handler import DbHandler
from readers.json_reader import JsonReader

path_to_json = os.path.join("dataset", "factbook_json")
json_files = [os.path.join(path_to_json, pos_json) for pos_json in os.listdir(path_to_json) if
              pos_json.endswith('.json')]

db_handler = DbHandler()
json_reader = JsonReader()
# analyzer = CountriesDictAnalyzer(db_handler)
analyzer = EthnicsDictAnalyzer(db_handler)

for file in json_files:
    analyzer.analyze_dict(json_reader.read_file(file))

db_handler.flush_to_db(Tables.COUNTRIES_TABLE)
