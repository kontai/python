from datetime import datetime,date,time

now=time(12)
today=date.today()
combine=datetime.combine(today,now)
print(combine)
print(combine.date())
print(combine.time())