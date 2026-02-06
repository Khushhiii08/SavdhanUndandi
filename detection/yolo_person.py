from ultralytics import YOLO # type: ignore

model = YOLO("models/yolov8n.pt")

def detect_people(frame):
    persons = []
    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if model.names[cls] == "person" and conf > 0.6:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                persons.append((x1, y1, x2, y2, conf))

    return persons