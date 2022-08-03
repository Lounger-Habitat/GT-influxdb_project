from datetime import datetime, time
from time import sleep
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS, os
from pytz import utc

from tool import progress_bar

bucket = "allTime"
org = "RStudio"
token = "AcmXNCiLXX68WD79t5_xJLDHfepaDeKoKmj3OWxOznagSzhDqWyNER3FewuU2Xhy4q4WrmGVFbrSjFx8jJRUqw=="
url = "http://localhost:8086"
client =influxdb_client.InfluxDBClient(url=url,bucket=bucket,token=token)


write_api = client.write_api(write_options=SYNCHRONOUS)
#本地时间
# dt_loc = datetime.strptime("2022-7-29 15:55:00", "%Y-%m-%d %H:%M:%S")
# # 本地时间转UTC时间
# dt_utc = dt_loc.astimezone(utc)
# p = influxdb_client.Point("my_measurement").tag("location","Prague").field("temperature",21.55).time(dt_utc)
# print('Point data',p)
# res = write_api.write(bucket=bucket,org=org,record=p)
# print('log-info:',res)
# client.close()


filename = 'zf_consume.csv'


filesize = os.path.getsize(filename)

load_bar = progress_bar(filesize)
load_bar.__next__()

send_size = 0
with open(filename) as f:
    
    header=f.readline()
    header = header.replace('\n','').split(',')
    send_size+=len(header)
    load_bar.send(send_size)
    for data in f.readlines():
        send_size+=len(data)+3
        data_handle = data.replace('\n','').split(',')
        # 本地时间
        dt_loc = datetime.strptime(data_handle[6], "%Y-%m-%dT%H:%M:%SZ")
        # 本地时间转UTC时间
        dt_utc = dt_loc.astimezone(utc)
       
        p = influxdb_client.Point("zf_consume").tag("device_id",data_handle[1]).tag("type",data_handle[4]).field("quantity",float(data_handle[2])).field("total",float(data_handle[3])).time(dt_utc)
        write_api.write(bucket=bucket,org=org,record=p)
        load_bar.send(send_size)
client.close()
