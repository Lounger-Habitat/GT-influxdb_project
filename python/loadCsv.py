import os
from time import sleep
import influxdb_client
from datetime import datetime
from pytz import utc
from tool import progress_bar


filename = 'dataEle.csv'


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
        dt_loc = datetime.strptime(data_handle[4], "%Y-%m-%dT%H:%M:%SZ")
        # 本地时间转UTC时间
        dt_utc = dt_loc.astimezone(utc)
       
        p = influxdb_client.Point("my_measurement").tag("device_id",data_handle[0]).tag("type",data_handle[3]).field("quantity",data_handle[1]).field("total",data_handle[2]).time(dt_utc)

        load_bar.send(send_size)
        