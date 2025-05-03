import cv2
import numpy as np
from pyzbar import pyzbar
import json
import os.path
from datetime import datetime

cap = cv2.VideoCapture("rtsp://your_rtsp_url") #canlı wifi ile görüntü sağlanması konumunda rtsp prokolü kullanılacağı takdirde bu kullanılır, bunun yerine bilgisayar kameranızı veya istediğinz bir videonun path'ini kullanınız
scanner = pyzbar.Scanner()
last_qr_time = 0
json_path = os.path.join(os.path.expanduser("~"), "Desktop", "qr_data.json")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_codes = scanner.scan(gray)

    if qr_codes:
        qr_data = qr_codes[0].data.decode("utf-8")
        qr_type = qr_codes[0].type
        current_time = cv2.getTickCount()
        elapsed_time = (current_time - last_qr_time) / cv2.getTickFrequency()

        if elapsed_time > 30:
            print("Detected {} code: {}".format(qr_type, qr_data))
            now = datetime.now()
            time_data = {
                "saat": now.hour,
                "dakika": now.minute,
                "saniye": now.second,
                "milisaniye": int(now.microsecond / 1000)
            }

            with open(json_path, 'a') as json_file:
                json_data = {
                    "kamikazeBaslangicZamani": time_data,
                    "kamikazeBitisZamani": time_data,
                    "qrMetni": qr_data
                }
                json.dump(json_data, json_file)
                json_file.write('\n')

            last_qr_time = current_time

    for qr_code in qr_codes:
        x, y, w, h = qr_code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("QR Code Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
