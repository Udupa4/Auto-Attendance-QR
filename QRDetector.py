import cv2

from datetime import datetime
import pytz

# Importing initial USN data
from USN_data import Dict

IST = pytz.timezone("Asia/Kolkata")

todayDate = datetime.now(IST).strftime("%d-%m-%Y")

# Define start and end Time
from start_end_Time import Start_End_Time
startTime, endTime = Start_End_Time(4)

camera_id = 0
delay = 3
window_name = "OpenCV QR Code"

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

while True:
    datetime_ist = datetime.now(IST)
    currentTime = datetime_ist.strftime("%H:%M:%S")

    if currentTime == startTime:
        print("Attendance started at:- ", todayDate, " ; ", currentTime)
        while True:
            ret, frame = cap.read()

            if ret:
                ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)

                if ret_qr:
                    for s, p in zip(decoded_info, points):
                        if s:
                            color = (0, 255, 0)
                            if Dict[s] == False:
                                Dict[s] = True
                                print(s)
                        else:
                            color = (0, 0, 255)
                        frame = cv2.polylines(
                            frame, [p.astype(int)], True, color, 8)

                cv2.imshow(window_name, frame)

            datetime_ist = datetime.now(IST)
            currentTime = datetime_ist.strftime("%H:%M:%S")
            if currentTime == endTime or cv2.waitKey(delay) & 0xFF == ord("q"):
                print("Attendance ended at:- ", todayDate, " ; ", currentTime)
                break

        cv2.destroyWindow(window_name)

        print("Today's attendance:- ")
        print(Dict)

        # Updating the attendance to excel file
        from update_to_Excel import update_data_to_excel
        
        file_name = "./Attendance.xlsx"
        update_data_to_excel(file_name, Dict)
        print("Updated to excel successfully")
        
