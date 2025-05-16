# Exercice: Time Delta
# URL: https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
# Description: We are given two dates with a time in hours, minutes and seconds as well as a time zone. 
# The aim is to retrieve the absolute difference between them

from datetime import datetime

def time_delta(t1, t2):
    timestamp_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, timestamp_format)
    time2 = datetime.strptime(t2, timestamp_format)
    delta = abs(int((time1 - time2).total_seconds()))
    return delta
