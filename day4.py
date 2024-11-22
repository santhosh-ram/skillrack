from datetime import *
def next_day(n):
  curr_date=datetime.strptime(n,"%d-%m-%Y")
  next_date=curr_date+timedelta(days=7)
  return next_date.strftime("%d-%m-%Y")
n=input().strip()
print(next_day(n))
