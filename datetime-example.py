from datetime import datetime
import time

today = datetime.today()
print(today)
today_str = today.strftime("%d/%B/%Y %H:%M:%S")
today_date_obj = datetime.strptime(today_str, "%d/%B/%Y %H:%M:%S")

print("today_str",today_str)
print("today type", type(today_str))

print("today_date_obj", today_date_obj)
print("today_date_obj type", type(today_date_obj))
