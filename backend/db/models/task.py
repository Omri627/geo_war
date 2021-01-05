from db.dal_queries.countries_queries import CountriesQueries
from pydantic import BaseModel
import threading

class Task:
    method: any
    arguments: tuple
    is_done: threading.Event
    return_value: any

    def __init__(self, method: any, arguments: tuple):
        # initialize country data
        self.method = method
        self.arguments = arguments
        self.return_value = None
        self.is_done = threading.Event()
        self.is_done.clear()

    def activate(self):
        # activate the task
        self.return_value = self.method(*self.arguments)
        self.is_done.set()

    def wait(self):
        # wait till the task is completed
        self.is_done.wait()
        return self.return_value
