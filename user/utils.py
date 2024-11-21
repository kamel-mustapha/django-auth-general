import datetime

def get_time_delta(hours=1):
    current_time = datetime.datetime.now()
    expiration_time = current_time + datetime.timedelta(hours=hours)
    exp_timestamp = int(expiration_time.timestamp())
    return exp_timestamp