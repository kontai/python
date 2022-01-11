from datetime import date, timedelta

# day的範圍 (1-1-1)~(9999-12-31)
now = date.today()
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
after_2_day = now + 18 * one_day
print(after_2_day)
yesterday = now - one_day
print(yesterday)
