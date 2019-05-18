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


# Timezone with Pendulum-------------
print('\n')
import pendulum     # https://pendulum.eustace.io/

DEFAULT_TIMEZONE = 'UTC'    # GMT+0

local_datetime = pendulum.now()
utc = pendulum.now('UTC')
print('Local datetime:', local_datetime)
print('Time in UTC:', utc)

init_dt = pendulum.datetime(1992, 7, 10, tz='America/Chicago')
print('Init datetime:', init_dt)

print('Get local timezone:', local_datetime.timezone_name)
print('Difference from UTC:', local_datetime.offset_hours)  # if Asia/Jakarta(UTC+7) return 7.0
print('Is local timezone?', init_dt.is_local())
