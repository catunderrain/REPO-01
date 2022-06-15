class people:

    def __init__(self, peo_name, peo_height):
        self.name = peo_name
        self.height = peo_height

    def peoInfo(self):
        print('This is ' + self.name + ', height is ' + self.height)


a = people('VA', '180')
a.peoInfo()
