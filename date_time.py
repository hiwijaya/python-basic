from datetime import datetime, timedelta, date, time


now = datetime.now()

d = now.date()      # return date object
t = now.time()      # return time object

print('Weekday:', d.weekday())     # 0=Monday, 6=Sunday
print('Day:', d.day)
print('Month:', d.month)
print('Year:', d.year)


# init -----------------
print('New date:', date(1992, 7, 10))     # date(year, month, day)
print('New time:', time(1, 20, 30))     # time(hour, minute, second, microsecond)


# Formatting -----------
print('Today:', d)
print('Formatted date:', d.strftime('%a, %d-%m-%Y'))            # Fri, 17-05-2019
print('Formatted time:', t.strftime('%H:%M:%S | %I.%M %p'))     # 15:17:35 | 03.17 PM
print('ISO 8601:', now.isoformat())


# Timedelta ------------
print('Today:', d)
print('Tomorrow:', d + timedelta(days=1))
print('Tomorrow by hours:', now + timedelta(hours=9))   # tips: use datetime instead only date/time, coz the value is more details

print('Now:', t)
print('Next hour:', (now + timedelta(hours=1)).time())


# Timezone -------------
import pendulum     # https://pendulum.eustace.io/

DEFAULT_TIMEZONE = 'UTC'    # GMT+0

print('Now:', pendulum.now(DEFAULT_TIMEZONE))
