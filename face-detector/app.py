import os
import cv2
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)

def detect_faces(frame):
    # Load the pre-trained Haar Cascade face detection classifier
    # haarcascade_eye.xml detects eyes 
    # haarcascade_frontalface_default.xml detects face
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

def generate_frames():
    # Get the RTSP URL from the environment variable
    rtsp_url = os.getenv("RTSP_URL")

    #rtsp_url = 'rtsp://darryl:cauldwell@192.168.188.3/stream2'
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Failed to open RTSP stream.")
    else:
      print("RTSP stream opened successfully.")

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = detect_faces(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
