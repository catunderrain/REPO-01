# **kwargs : dictionary
def day(**date):
    print('Today is ')
    for a, b in date.items():
        print(b)
        
day(day = 16, month = 11, year = 2001)