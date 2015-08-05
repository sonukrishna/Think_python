'''program that gets the current date and prints the day of
the week.'''



import datetime

days={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
def present_day():
    today=datetime.date.today()
    return today.isoweekday()
def day():
    today=present_day()
    print days[today]
print present_day()
day()

