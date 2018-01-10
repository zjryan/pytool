# -*- coding: utf-8 -*-
import time

try:
    basestring
except NameError:
    basestring = str


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


class Time(object):
    default_format = "%Y-%m-%d %H:%M:%S"
    def __init__(self, time, fmt=None):
        if fmt:
            self.default_format = fmt
        if isinstance(time, (int, float)):
            if time < 0:
                raise ValueError('init param time except be a utc timestamp')
            self.timestamp = time
            self.datetime = datetime_helper(time, self.default_format)
        elif isinstance(time, basestring):
            self.timestamp = timestamp_helper(time, self.default_format)
            self.datetime = time
        else:
            raise ValueError('init param time except be a utc timestamp or'
                             'a datetime string, got {}'.format(time))


def diff_set(s1, s2):
    return s1.difference(s2).union(s2.difference(s1))
