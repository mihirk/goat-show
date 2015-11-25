class Schedule(object):
    def __init__(self, number_of_days):
        self.number_of_days = number_of_days
        self.performances = {str(day + 1): [] for day in range(number_of_days)}

    def schedule_on(self, animals, day):
        self.performances[str(day + 1)] = animals.can_perform(day)

    def schedule_with(self, animals):
        return {day: self.schedule_on(animals, day) for day in range(self.number_of_days)}

    def get(self):
        return {day: ', '.join(map(str, self.performances[day])) for day in self.performances.iterkeys()}
