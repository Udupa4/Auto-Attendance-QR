import datetime
import pytz

def Start_End_Time(seconds=5):
    IST = pytz.timezone("Asia/Kolkata")

    current_time = datetime.datetime.now()

    # Define a time increment (in this case, 30 seconds)
    time_increment = datetime.timedelta(seconds=seconds)

    # Calculate a new time by adding the time increment to the current time
    start_time = current_time + time_increment
    end_time = current_time + 5 * time_increment

    return start_time.strftime("%H:%M:%S"), end_time.strftime("%H:%M:%S")

# start_time, end_time = Start_End_Time()
# print(start_time)
# print(end_time)