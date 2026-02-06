import time

person_tracker = {}

def compute_risk(person_id, pose_data):
    risk = 0.0

    if pose_data is None:
        return risk

    if pose_data["wrist_motion"] > 0.15:
        risk += 0.4

    if pose_data["hand_above_shoulder"]:
        risk += 0.3

    return min(risk, 1.0)

def check_loitering(person_id):
    now = time.time()

    if person_id not in person_tracker:
        person_tracker[person_id] = now
        return False

    return (now - person_tracker[person_id]) > 25

