# -*- coding: utf-8 -*-
import time


# 转换格式为'2016-09-26 10:10:20'的时间为时间戳
def timestamp_helper(datetime, format="%Y-%m-%d %H:%M:%S"):
    if datetime == '':
        return 0
    time_array = time.strptime(datetime, format)
    time_stamp = int(time.mktime(time_array))
    return time_stamp


# 将时间戳转为时间字符串
def datetime_helper(timestamp, format="%Y-%m-%d %H:%M:%S"):
    local_time = time.localtime(timestamp)
    time_str = time.strftime(format, local_time)
    return time_str
