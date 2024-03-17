# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:13:12 2024

@author: iamrs
"""

import datetime
import pytz
import time

def get_est_time():
    # Get the current time in Eastern Standard Time (EST) zone
    est_zone = pytz.timezone('US/Eastern')
    est_time = datetime.datetime.now(est_zone)
    return est_time

def set_alarm():
    print("Set your alarm:")
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minute (0-59): "))
    # Create a datetime object for the alarm time
    alarm_time = get_est_time().replace(hour=hour, minute=minute, second=0, microsecond=0)
    return alarm_time

def main():
    alarm_time = set_alarm()
    print("Alarm set for:", alarm_time.strftime("%H:%M"))

    while True:
        current_time = get_est_time()
        print("Current EST time:", current_time.strftime("%H:%M:%S"), end="\r")
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            print("\nWake up! It's time for your alarm!")
            break
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
