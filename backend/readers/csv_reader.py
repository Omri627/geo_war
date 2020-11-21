import csv
from typing import List

from readers.file_reader import FileReader
from utils.logger_provider import LoggerProvider


class CsvReader(FileReader):

    def __init__(self, headers: List[str]) -> None:
        super().__init__()
        self.logger = LoggerProvider.get_logger(__name__)
        self._headers = headers

    def read_file(self, path: str) -> List[dict]:
        data_list_dict = list()
        with open(path, newline='', encoding="utf8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                row_dict = dict(zip(self._headers, [row[header] for header in self._headers]))
                data_list_dict.append(row_dict)
        return data_list_dict
