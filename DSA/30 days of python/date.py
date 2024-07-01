from datetime import datetime, date

now = datetime.now()
print(now)
month = now.month
print(month)
timestamp = now.timestamp()
# print(timestamp)

'''difference bw two points in time'''
today = date(year=2024,month=7,day=1)
birth_Date = date(year=2001,month=1,day=3)
age = today - birth_Date