import os

from analyzers.countries_analyzer import CountriesDictAnalyzer
from analyzers.ethincs_analyzer import EthnicsDictAnalyzer
from analyzers.language_analyzer import LanguageDictAnalyzer
from analyzers.religions_analyzer import ReligionsDictAnalyzer
from db.dal_quries.tables import Tables
from db.db_handler import DbHandler
from readers.json_reader import JsonReader

path_to_json = os.path.join("dataset", "factbook_json")
json_files = [os.path.join(path_to_json, pos_json) for pos_json in os.listdir(path_to_json) if
              pos_json.endswith('.json')]

db_handler = DbHandler()
json_reader = JsonReader()
analyzers = [CountriesDictAnalyzer(db_handler), EthnicsDictAnalyzer(db_handler), LanguageDictAnalyzer(db_handler),
             ReligionsDictAnalyzer(db_handler)]

for file in json_files:
    raw_data = json_reader.read_file(file)
    for analyzer in analyzers:
        analyzer.analyze_dict(raw_data)

db_handler.flush_to_db(Tables.COUNTRIES_TABLE)
db_handler.flush_to_db(Tables.ETHNICS_TABLE)
db_handler.flush_to_db(Tables.LANGUAGES_TABLE)
db_handler.flush_to_db(Tables.RELIGION_TABLE)
