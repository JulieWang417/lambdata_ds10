# part 1

from random import randint


class Product():
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = randint(1000000, 9999999)

# part2


class Product():
    def __init__(self, name, price, weight, flammability):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        if ratio < 1 and ratio >= 0.5:
            return "Kinda stealable..."
        else:
            return "Very stealable!"

    def explode(self):
        product = self.weight * self.flammability
        if product < 10:
            return "...fizzle"
        if product >= 10 and product < 50:
            return "...boom!"
        else:
            return "BABOOM!"

# part 3


class BoxingGlove(Product):
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH"
