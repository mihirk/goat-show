import json


class Software(object):
    def __init__(self, data, number):
        self.number = number
        with open(data, 'r') as f:
            self.data = json.load(f)

    def do_magic(self):
        for i in range(0, self.number):
            names = ""
            for j in range(0, len(self.data)):
                if i % (self.data[j]["rest"] + 1) == 0:
                    names += self.data[j]["name"] + ", "
            if names != "":
                print "{} can perform on day {}".format(names[:-2], i + 1)
            else:
                print "Goats be tired on day {} yo".format(i + 1)


Software("../goats.json", 10).do_magic()
