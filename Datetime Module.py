import datetime

help(datetime.date) 

dt=datetime.date(1996,5,17)  
print(dt) 
1996-05-17

a=dt.day

print(dt.day) 
print(dt.month) 
print(dt.year) 

# String with date datas

message= 'Good Mornig today date is {:%A,%B %d,%Y}.'
print(message.format(dt))

launch_date = datetime. date (2017, 3, 30)
launch_time = datetime. time (22, 27, 0)
launch_datetime = datetime. datetime (2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)


print(launch_time.hour)
print(launch_time.min)
print(launch_time.second)
print(launch_time.microsecond)

print(launch_datetime.hour)
print(launch_datetime.min)
print(launch_datetime.second)
print(launch_datetime.microsecond)

# To print todays date
now=datetime.datetime.today()

# String to datetime
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
