import threading
import cv2
import time
import os
from flask import Flask, Response, render_template, jsonify, send_from_directory
from dotenv import load_dotenv
from detect import detect_from_camera

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Global shared resources
initial_camera_indices = [0, 1]  # Initial list to test (adjust as needed)
frames_dict = {}
locks_dict = {}
alerts_list = []
alerts_lock = threading.Lock()

# Test camera availability
def test_camera(cam_id):
    cap = cv2.VideoCapture(cam_id)
    if not cap.isOpened():
        print(f"❌ Could not open Camera {cam_id}")
        cap.release()
        return False
    cap.release()
    return True

# Filter working cameras
camera_indices = [cam_id for cam_id in initial_camera_indices if test_camera(cam_id)]
for cam_id in camera_indices:
    frames_dict[cam_id] = None
    locks_dict[cam_id] = threading.Lock()

# Synchronization barrier (adjusted for working cameras)
barrier = threading.Barrier(len(camera_indices)) if camera_indices else None

# Route for the dashboard
@app.route('/')
def index():
    return render_template('index.html', camera_indices=camera_indices)

# Route for video streaming
@app.route('/stream/<int:cam_id>')
def stream(cam_id):
    def generate_frames():
        while True:
            with locks_dict[cam_id]:
                frame = frames_dict[cam_id]
            if frame is not None:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)  # Adjust for frame rate
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for alerts
@app.route('/alerts')
def get_alerts():
    with alerts_lock:
        alerts = alerts_list[-10:]  # Last 10 alerts
    return jsonify(alerts)

# Route for serving snapshots
@app.route('/snapshots/<path:filename>')
def serve_snapshot(filename):
    return send_from_directory('snapshots', filename)

if __name__ == '__main__':
    # Start detection threads for working cameras only
    threads = []
    if camera_indices:
        for cam_id in camera_indices:
            t = threading.Thread(target=detect_from_camera, args=(cam_id, barrier, frames_dict, locks_dict, alerts_list, alerts_lock))
            t.start()
            threads.append(t)
    else:
        print("No working cameras available.")

    # Run Flask app
    app.run(host='0.0.0.0', port=5000, threaded=True)