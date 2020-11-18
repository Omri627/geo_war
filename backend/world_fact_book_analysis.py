import os

from analyzers.countries_analyzers import CountriesDictAnalyzer
from readers.json_reader import JsonReader

path_to_json = os.path.join("dataset", "factbook_json")
json_files = [os.path.join(path_to_json, pos_json) for pos_json in os.listdir(path_to_json) if
              pos_json.endswith('.json')]
json_reader = JsonReader()
analyzer = CountriesDictAnalyzer()
for file in json_files:
    analyzer.analyze_dict(json_reader.read_file(file))
