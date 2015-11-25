import json

from show.animals import Animals
from show.schedule import Schedule
from pprint import pprint


class JSONReader(object):
    @staticmethod
    def read(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)


class Controller(object):
    def __init__(self, data_files, number_of_days):
        self.animals = self.read_data(data_files)
        self.schedule = Schedule(number_of_days)

    def read_data(self, data_files):
        animals_data = map(lambda animal: {"type": animal["type"], "data": JSONReader.read(animal["path"])}, data_files)
        return map(lambda animal_data:
                   Animals.factory(animal_data),
                   animals_data)

    def run(self):
        map(self.schedule.schedule_with, self.animals)
        return self.schedule.get()


print Controller([{"type": "Goat", "path": "../goats.json"}], 10).run()