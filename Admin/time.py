import time
import datetime

def now():
    now = datetime.datetime.now().isoformat() + "Z"
    return now