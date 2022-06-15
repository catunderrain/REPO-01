class animal:
    def __init__(self, typ, name, age, color, option):
        self.typ = typ
        self.name = name
        self.age = age
        self.color = color
        self.option = option

    def say(self):
        print('This is a {}, her name is {}, she is {} years old!'.format(
            self.typ, self.name, self.age))


a = animal('human', 'VA', '21', 'red', '')
print(a.age)
del a.age
print(a.age)
