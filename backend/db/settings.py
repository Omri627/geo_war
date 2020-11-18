import json
import os


class Settings:
    SETTINGS_FILE = os.path.join("db", "db_settings.json")

    def __init__(self):
        settings = self._get_settings_from_file()
        self.host = settings['host']
        self.user = settings['user']
        self.password = settings['password']

    def _get_settings_from_file(self) -> dict:
        with open(self.SETTINGS_FILE) as f:
            settings_dict = json.load(f)
        return settings_dict
