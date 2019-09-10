import time
import os
import datetime
# from datetime import datetime,timedelta

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

print datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
# URL https://www.tutorialspoint.com/python/time_strftime.htm
# %a - abbreviated weekday name
# %A - full weekday name
# %b - abbreviated month name
# %B - full month name
# %c - preferred date and time representation
# %C - century number (the year divided by 100, range 00 to 99)
# %d - day of the month (01 to 31)
# %D - same as %m/%d/%y
# %e - day of the month (1 to 31)
# %g - like %G, but without the century
# %G - 4-digit year corresponding to the ISO week number (see %V).
# %h - same as %b
# %H - hour, using a 24-hour clock (00 to 23)
# %I - hour, using a 12-hour clock (01 to 12)
# %j - day of the year (001 to 366)
# %m - month (01 to 12)
# %M - minute
# %n - newline character
# %p - either am or pm according to the given time value
# %r - time in a.m. and p.m. notation
# %R - time in 24 hour notation
# %S - second
# %t - tab character
# %T - current time, equal to %H:%M:%S
# %u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
# %U - week number of the current year, starting with the first Sunday as the first day of the first week
# %V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
# %W - week number of the current year, starting with the first Monday as the first day of the first week
# %w - day of the week as a decimal, Sunday=0
# %x - preferred date representation without the time
# %X - preferred time representation without the date
# %y - year without a century (range 00 to 99)
# %Y - year including the century
# %Z or %z - time zone or name or abbreviation
# %% - a literal % character




# ================ Comparing file access dates in python
# To convert it to a datetime object that represents time in UTC, 
# call datetime.utcfromtimestamp() method.

# Do not confuse a string representation of an object and the object
# itself. Do not compare time/date as strings, use objects instead.

# from datetime import datetime, timedelta
now = datetime.datetime.utcnow()
file = __file__
file_time = datetime.datetime.utcfromtimestamp(os.path.getmtime(file))
time_diff = now - file_time
print "file_time - {}".format(file_time)
if (time_diff) > datetime.timedelta(1): 
    print("more than a day has passed")
# -----------------------------------------------------------


# =========== how to format timedelta 
totalSeconds = time_diff.seconds
hours, remainder = divmod(totalSeconds, 3600)
minutes, seconds = divmod(remainder, 60)
print 'hours %s: minutes %s: seconds %s' % (hours, minutes, seconds)
hours,minutes,seconds = ["{:02d}".format(x) for x in [hours,minutes,seconds]]
print 'hours:%s minutes:%s seconds:%s formatted' % (hours, minutes, seconds)


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

from string import Formatter
def strfdelta(tdelta, fmt):
    f = Formatter()
    d = {}
    l = {'D': 86400, 'H': 3600, 'M': 60, 'S': 1}
    k = map( lambda x: x[1], list(f.parse(fmt)))
    rem = int(tdelta.total_seconds())

    for i in ('D', 'H', 'M', 'S'):
        if i in k and i in l.keys():
            d[i], rem = divmod(rem, l[i])

    return f.format(fmt, **d)

# Oddly, this did not work for me as written, 
# I had to change map( lambda x: x[1], list(f.parse(fmt))) 
# to list(map( lambda x: x[1], list(f.parse(fmt))))