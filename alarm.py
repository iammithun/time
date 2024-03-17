# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:08:39 2024

@author: iamrs
"""

import datetime
import pytz
import time
from playsound import playsound

def get_chicago_time():
    # Get the current time in UTC
    utc_now = datetime.datetime.utcnow()

    # Set the UTC time zone
    utc_zone = pytz.timezone('UTC')

    # Convert UTC time to Chicago time
    chicago_zone = pytz.timezone('America/Chicago')
    chicago_time = utc_now.replace(tzinfo=utc_zone).astimezone(chicago_zone)

    return chicago_time

def set_alarm():
    print("Set your alarm:")
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minute (0-59): "))

    # Create a datetime object for the alarm time
    alarm_time = get_chicago_time().replace(hour=hour, minute=minute, second=0, microsecond=0)

    return alarm_time

def main():
    alarm_time = set_alarm()
    print("Alarm set for:", alarm_time.strftime("%H:%M"))

    while True:
        current_time = get_chicago_time()
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            print("Wake up! It's time for your alarm!")
            playsound("alarm_sound.mp3")  # Replace "alarm_sound.mp3" with your alarm sound file
            break
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
