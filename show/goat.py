from show.animal import Animal


class Goat(Animal):
    def __init__(self, name, rest):
        super(Goat, self).__init__(name)
        self.rest_required = rest

    def can_perform(self, day):
        return day == 0 or day % (self.rest_required + 1) == 0
