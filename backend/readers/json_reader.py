import json

from readers.file_reader import FileReader


class JsonReader(FileReader):

    def read_file(self, path: str) -> dict:
        with open(path, encoding="utf8") as f:
            data_dict = json.load(f)
        return data_dict
