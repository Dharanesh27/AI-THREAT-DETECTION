# AI-Powered Weapon Detection & Camera Tampering Alert System

An intelligent surveillance system that uses Computer Vision and Deep Learning to detect weapons and camera tampering in real time. The system analyzes live CCTV feeds using a custom YOLO model and instantly notifies authorized personnel when suspicious activity is detected.

## Features

* Real-time weapon detection using YOLO
* Full and partial camera blockage detection
* Multi-camera monitoring support
* Automatic snapshot capture on incidents
* Email alerts with evidence images
* SMS notifications using Twilio
* Event logging with timestamps
* Secure configuration using environment variables

## Tech Stack

* Python
* OpenCV
* YOLO (Ultralytics)
* NumPy
* Flask
* Twilio API
* SMTP Email Services

## Project Structure

```text
├── main.py
├── app.py
├── detect.py
├── weapon_detect.pt
├── templates/
├── snapshots/
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Dharanesh27/AI-THREAT-DETECTION.git
cd AI-THREAT-DETECTION
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver@gmail.com

TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_token
TWILIO_FROM=your_twilio_number
TWILIO_TO=recipient_number
```

4. Place the trained YOLO model file (`weapon_detect.pt`) in the project directory.

## Usage

Run the application:

```bash
python main.py
```

or

```bash
python app.py
```

The system will:

* Monitor live camera feeds
* Detect weapons in real time
* Detect camera obstruction attempts
* Capture snapshots of incidents
* Send Email and SMS alerts
* Maintain event logs

## Applications

* Smart Surveillance Systems
* Educational Institutions
* Corporate Offices
* Public Safety Monitoring
* Airports and Transportation Hubs
* Industrial Security

## Future Enhancements

* Cloud-based monitoring dashboard
* Mobile application integration
* Face recognition support
* Database-backed incident management
* Advanced threat classification
  
## 🎥 Demo Video

Watch the project demo here:
🔗 https://drive.google.com/file/d/1xCag4eqAUZ9lCQ5n_C86QDyxCvlwNAS4/view?usp=drive_link

## License

This project is intended for educational and research purposes.
