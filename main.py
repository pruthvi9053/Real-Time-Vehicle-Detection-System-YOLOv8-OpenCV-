import cv2
import time
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("Vehicle Detection\yolov8n.pt")

# Vehicle class IDs (from COCO dataset)
vehicle_classes = {2: "Car", 3: "Motorcycle", 5: "Bus", 7: "Truck"}

# Colors for each vehicle type
colors = {
    "Car": (0, 255, 0),          # Green
    "Motorcycle": (0, 255, 255), # Yellow
    "Bus": (255, 0, 0),          # Blue
    "Truck": (0, 0, 255)         # Red
}

# Load video
video_path = "Vehicle Detection\Traffic4.mp4"
cap = cv2.VideoCapture(video_path)

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time

    # Model prediction
    results = model(frame, stream=True)

    # Vehicle count
    count = {"Car": 0, "Motorcycle": 0, "Bus": 0, "Truck": 0}

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            if cls_id in vehicle_classes and conf > 0.4:  # filter + confidence
                vehicle_type = vehicle_classes[cls_id]
                count[vehicle_type] += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                color = colors[vehicle_type]

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{vehicle_type} {conf:.2f}",
                            (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display FPS on screen
    cv2.putText(frame, f"FPS: {int(fps)}", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Display count
    y_offset = 60
    for v in count:
        cv2.putText(frame, f"{v}: {count[v]}", (20, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[v], 2)
        y_offset += 30

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
