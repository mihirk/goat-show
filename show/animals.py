from show.crocodile import Crocodile
from show.goat import Goat

types = {
    "Goat": Goat,
    "Crocodile": Crocodile
}


class Animals(object):
    def __init__(self, type, animals):
        self.type = type
        self.animals = animals

    @classmethod
    def factory(cls, animal_data):
        animals = map(lambda data: types[animal_data["type"]].factory(data),
                      animal_data["data"])
        return cls(animal_data["type"], animals)

    def can_perform(self, day):
        return filter(lambda animal: animal.can_perform(day), self.animals)

    def __str__(self):
        return "{} : {}".format(self.type, self.animals)

    def __repr__(self):
        return str(self.__dict__)
