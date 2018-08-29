class Person:
    def __init__(self, name, origin, age, isSitting, ownedRobot):
        self.name = name
        self.origin = origin
        self.age = age
        self.isSitting = isSitting
        self.ownedRobot = ownedRobot
    def introduceSelf(self):
        print('My name is', self.name)
        print('I\'m from', self.origin)
        print('I\'m', self.age, 'years old')
    def sit_down(self):
        self.isSitting = True
    def stand_up(self):
        self.isSitting = False
class Robot:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def introduceSelf(self):
        print('My name is', self.name)

r = Robot('Krusanity', 'Black', 69)
p = Person('mKay', 'Egypt', 20, False, 'r')
r.introduceSelf()
a = p.ownedRobot
a.introduceSelf()
