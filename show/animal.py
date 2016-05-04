class Animal(object):
    def __init__(self, name):
        self.name = name

    def can_perform(self, day):
        pass

    @classmethod
    def factory(cls, animal_data):
        return cls(**animal_data)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
