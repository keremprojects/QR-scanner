## 📷 Lightweight QR Code Scanner

This script captures a live video stream (RTSP) and scans for QR codes in real time using `pyzbar` and `OpenCV`.  
If a QR code is detected, its content and timestamp are stored in a JSON file (default: on Desktop).  
To reduce duplicates, the scanner saves only one QR read every 30 seconds.

### 🛠️ Technologies
- Python
- OpenCV
- pyzbar
- JSON

### ⚙️ How It Works
- Connects to an RTSP video stream or your desired source of video
- Converts each frame to grayscale.
- Scans the frame for QR codes.
- If a QR is detected, logs it with a timestamp to `qr_data.json`.

### ▶️ How to Run

1. Install the required packages:
   
   pip install opencv-python pyzbar numpy
   edit the source to your liking
   run the script
