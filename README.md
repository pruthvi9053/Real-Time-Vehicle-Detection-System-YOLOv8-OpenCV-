# 🚗 Real-Time Vehicle Detection & Counting System (YOLOv8 + OpenCV)

This project is a real-time Vehicle Detection System built using YOLOv8 and OpenCV, designed to detect and count different vehicle types from traffic video footage.

It highlights the ability to detect only specific vehicle classes, draw colored bounding boxes, calculate FPS, and display vehicle counts live on screen — making it suitable for smart traffic, surveillance, and analytics use cases.




---

## ✨ Key Features

This system is designed to provide quick, actionable insights into traffic composition and flow.

| Feature | Description | Benefit |
| :--- | :--- | :--- |
| **Selective Vehicle Detection** | Detects only specified vehicle classes: **Car, Motorcycle, Bus, Truck**. | Filters out irrelevant objects (people, signs), focusing solely on traffic analysis. |
| **Colored Bounding Boxes** | Each vehicle type is assigned a distinct color (e.g., Green for Car, Red for Truck). | Enhances visual clarity and instant differentiation between vehicle types. |
| **Real-Time Counting** | Calculates and displays the count of each detected vehicle type live on the frame. | Provides immediate data for traffic density and composition analysis. |
| **FPS & Confidence Display** | Shows **Frames Per Second (FPS)** and detection **Confidence Score** on each box. | Allows for monitoring of system performance and detection reliability. |
| **Video Stream Support** | Processes video files (`.mp4`, etc.) and can be easily adapted for live camera feeds. | Versatile deployment capability for both recorded and live scenarios. |

---

## 🛠️ Technology Stack

The project relies on a few key technologies for its functionality and performance.

| Category | Tool / Library | Role in Project |
| :--- | :--- | :--- |
| **Programming Language** | **Python 3.x** | The core development language. |
| **Object Detection Model** | **YOLOv8** (via Ultralytics) | The primary engine for high-speed, accurate vehicle identification. |
| **Video Processing** | **OpenCV** (`cv2`) | Handles reading the video, drawing overlays, and displaying the output. |
| **Numerical Operations** | **NumPy** | Provides high-performance array and frame manipulation capabilities (backend support). |

---

## 📂 Project Structure

The repository is structured for clarity and easy execution:
Vehicle Detection/ │ ├── main.py # 🧠 Main execution script containing YOLOv8 and OpenCV logic. ├── yolov8n.pt # 🤖 Pre-trained YOLOv8 Nano model weights. ├── Traffic3.mp4 # 📹 Sample video file for demonstration. └── README.md # 📜 Project overview and setup instructions (this file).

