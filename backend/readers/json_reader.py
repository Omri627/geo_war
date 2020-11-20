import json

from readers.file_reader import FileReader
from utils.logger_provider import LoggerProvider


class JsonReader(FileReader):

    def __init__(self) -> None:
        super().__init__()
        self.logger = LoggerProvider.get_logger(__name__)

    def read_file(self, path: str) -> dict:
        with open(path, encoding="utf8") as f:
            self.logger.info(f"Opened file: {path}")
            data_dict = json.load(f)
        return data_dict
