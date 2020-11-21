import json
import os

from db.db_handler import DbHandler
from readers.csv_reader import CsvReader

db_handler = DbHandler()
analyzers = []


csv_reader = CsvReader(['name', 'nationality', 'position'])
soccer_dict = csv_reader.read_file(os.path.join('dataset', 'fifa', 'FIFA-21 Complete.csv'))
print(soccer_dict)
# for analyzer in analyzers:
#     analyzer.analyze_dict(soccer_dict)
