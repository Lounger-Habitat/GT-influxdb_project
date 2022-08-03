from datetime import datetime
from pytz import utc
import time
 
# 本地时间
dt_loc = datetime.strptime("2022-7-28 11:55:00", "%Y-%m-%d %H:%M:%S")
# 本地时间转UTC时间
dt_utc = dt_loc.astimezone(utc)
# UTC时间转本地时间
dt_loc1 = dt_utc.astimezone()

print('本地时间',dt_loc)
print('UTC时间',dt_utc.__str__())


# 字符串为UTC时间，需要调整到LOC时间，差值通过计算得到
# utc_dt = datetime.strptime("2021-11-05 08:00:00", "%Y-%m-%d %H:%M:%S")
# now_stamp = time.time()
# loc = datetime.fromtimestamp(now_stamp)
# utc = datetime.utcfromtimestamp(now_stamp)
# utc_offset = loc - utc
# loc_dt = utc_offset + utc_dt