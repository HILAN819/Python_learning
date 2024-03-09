from datetime import datetime, timedelta
import time

dt = datetime(2018, 12, 7) - timedelta(days=45)
# dt = datetime.now()
dd = datetime.strptime("2024/03/06", "%Y/%m/%d")
ds = datetime.fromtimestamp(time.time())
# print(f"{ds.year}")
# print(dd.strftime("%Y/%m"))

duration = dd - dt
print(duration)
print(duration.days)
print(duration.total_seconds())
print(dt)