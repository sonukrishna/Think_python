'''	incrementing the date by adding with a given intiger	  '''



class Date(object):
    "date object has atribute date,month,year"
date=Date()
date.date=11
date.month=7
date.year=1992

def print_date(date):
     return "date:month:year=> %.2d:%.2d:%.4d"%(date.date,date.month,date.year)


def days_in_month(date):
    if (date.month%2)!=0:
	days=31
    if((((date.month%2)==0)and(date.month)!=0)):
	days=30
    if date.month==2:
	days=28
    return days
def total_days(date):
    month=days_in_month(date)
    total=(date.year*365)+(date.month*month)+date.date   
    return total
def days_to_date(date,total):
    box=Date()
    box.year,days=divmod(total,365)
    month=days_in_month(date)
    box.month,box.date=divmod(days,month)
    return box
def increment_date(date,n):
    totaldays=total_days(date)+n
    print "the date changed after adding %d :" % n,
    return days_to_date(date,totaldays)
print 'the initial date is:',
print print_date(date)
new_date=increment_date(date,30000)
print print_date(new_date)
