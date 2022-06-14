# **kwargs : dictionary
def day(**date):
    print('Today is', end = ' ')
    for a, b in date.items():
        print(b, end = ' ')
        
day(day = 16, month = 11, year = 2001)