# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:18:05 2024

@author: iamrs
"""

import datetime
import pytz
import time
import sys

def get_est_time():
    # Get the current time in Eastern Standard Time (EST) zone
    est_zone = pytz.timezone('US/Eastern')
    est_time = datetime.datetime.now(est_zone)
    return est_time

def main():
    sys.stdout.write("Current time: ")
    sys.stdout.flush()
    while True:
        current_time = get_est_time()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        sys.stdout.write("\r{:02}:{:02}:{:02}".format(hours, minutes, seconds))
        sys.stdout.flush()
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()
