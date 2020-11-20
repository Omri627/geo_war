from abc import ABC, abstractmethod


class FileReader(ABC):

    @abstractmethod
    def read_file(self, path: str) -> dict:
        pass
