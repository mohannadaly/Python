class Person:
    def __init__(self, name, origin, age):
        self.name = name
        self.origin = origin
        self.age = age
    def introduceSelf(self):
        print('My name is', self.name)
        print('I\'m from', self.origin)
        print('I\'m', self.age, 'years old')
r = Person('mKay', 'Egypt', 20)
r.introduceSelf()
