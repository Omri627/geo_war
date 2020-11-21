import os

from analyzers.soccer_analyzer import SoccerListDictAnalyzer
from db.dal_quries.tables import Tables
from db.db_handler import DbHandler
from readers.csv_reader import CsvReader

db_handler = DbHandler()
analyzers = [SoccerListDictAnalyzer(db_handler)]

csv_reader = CsvReader(['name', 'nationality', 'team', 'position'])
soccer_dict = csv_reader.read_file(os.path.join('dataset', 'fifa', 'FIFA-21 Complete.csv'))
for analyzer in analyzers:
    analyzer.analyze_dict(raw_data=soccer_dict)
db_handler.flush_to_db(Tables.SOCCER_TABLE)
