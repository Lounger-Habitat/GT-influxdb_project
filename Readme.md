# Influxdb安装部署(windows环境)

1.官网下载rar([Install InfluxDB | InfluxDB OSS 2.3 Documentation (influxdata.com)](https://docs.influxdata.com/influxdb/v2.3/install/?t=Windows))

2.下载后解压，在文件夹内目录运行Windows PowerShell，直接运行./influxd.exe即可启动服务

<img src=".\image-20220712214701453.png" alt="image-20220712214701453" style="zoom:80%;" />

3.下载influx CLI([Install and use the influx CLI | InfluxDB OSS 2.3 Documentation (influxdata.com)](https://docs.influxdata.com/influxdb/v2.3/tools/influx-cli/?t=Windows))

4.配置influx CLI环境。

5.使用CLI命令连接服务

```sh
influx config create -n rookie-config -u http://localhost:8086 -t OSZs6x07yAreUHcYaKfkw_QpwSkNA9FGMMtOzGFTRaCCEWmB0ghiugV8XJ4HBzMRa61VvBQj8avPUmap7aTZlQ== -o rookie-org --active
```

连接成功后会显示如下：

![image-20220712215704979](D:.\image-20220712215704979.png)

# 处理水电表数据

- 将下载的zf_consume Excel数据转成csv

- 按照示例中格式给csv文件添加头注释![image-20220712220752039](D:.\image-20220712220752039.png)

# 将数据导入influxdb数据库

- Include annotations in the CSV file or inject them using the `--header` flag of the `influx write` command. See the examples below for more details.

  ##### Example write command

  ```sh
  influx write -b <bucket> -f path/to/example.csv
  ```

  ##### example.csv

  ```csv
  #datatype measurement,tag,double,dateTime:RFC3339
  m,host,used_percent,time
  mem,host1,64.23,2020-01-01T00:00:00Z
  mem,host2,72.01,2020-01-01T00:00:00Z
  mem,host1,62.61,2020-01-01T00:00:10Z
  mem,host2,72.98,2020-01-01T00:00:10Z
  mem,host1,63.40,2020-01-01T00:00:20Z
  mem,host2,73.77,2020-01-01T00:00:20Z
  ```

- 使用命令将数据导入数据库

- 导入后在数据库界面点击SCRIPT EDITOR

  ```flux
  //使用绝对时间
  from(bucket:"Jackbucket")
  	|> range(start: 2018-11-05T23:30:00Z, stop: 2018-11-06T00:00:00Z)
  ```

  

2022-8-3更新

- 使用python API将数据导入

  ![](.\Dingtalk_20220803173320.jpg)

​	
