import cv2  # type: ignore
from detection.yolo_person import detect_people
from detection.pose_analysis import analyze_pose
from detection.behaviour_logic import compute_risk, check_loitering
from alerts.alert_manager import raise_alert
from config import VIDEO_SOURCE, AGGRESSION_SCORE_THRESHOLD
import time

cap = cv2.VideoCapture(VIDEO_SOURCE)

# Track how long people stay in frame
person_time_tracker = {}
person_id = 0

def crowd_risk(num_people):
    if num_people >= 5:
        return 0.25
    elif num_people >= 3:
        return 0.15
    return 0.0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    persons = detect_people(frame)
    pose_data = analyze_pose(frame)

    # Crowd-based mild risk
    crowd_score = crowd_risk(len(persons))

    for (x1, y1, x2, y2, conf) in persons:
        person_id += 1
        now = time.time()

        # Track persistence
        if person_id not in person_time_tracker:
            person_time_tracker[person_id] = now

        time_in_frame = now - person_time_tracker[person_id]

        # Base risk from pose
        risk = compute_risk(person_id, pose_data)

        # Loitering risk
        if check_loitering(person_id):
            risk += 0.3

        # Persistence risk (soft)
        if time_in_frame > 15:
            risk += 0.15

        # Crowd risk
        risk += crowd_score

        # Clamp risk
        risk = min(risk, 1.0)

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Show risk score
        cv2.putText(
            frame,
            f"Risk: {risk:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        # Preventive alert
        if risk >= AGGRESSION_SCORE_THRESHOLD:
            raise_alert("Preventive Risk Detected", risk)
            cv2.putText(
                frame,
                "⚠️ PREVENTIVE ALERT",
                (x1, y2 + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

    cv2.imshow("SavdhanUndandi : Prevention AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()