from datetime import datetime

def time_delta(t1, t2):
    timestamp_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, timestamp_format)
    time2 = datetime.strptime(t2, timestamp_format)
    delta = abs(int((time1 - time2).total_seconds()))
    return delta
