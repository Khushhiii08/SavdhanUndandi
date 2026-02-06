import mediapipe as mp # type: ignore
import numpy as np # type: ignore
import cv2 # type: ignore

from mediapipe.tasks import python # type: ignore
from mediapipe.tasks.python import vision # type: ignore

# Load pose model
base_options = python.BaseOptions(
    model_asset_path="models/pose_landmarker_full.task"
)

options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE
)

pose_landmarker = vision.PoseLandmarker.create_from_options(options)

def analyze_pose(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = pose_landmarker.detect(image)

    if not result.pose_landmarks:
        return None

    lm = result.pose_landmarks[0]

    left_wrist = lm[15]
    right_wrist = lm[16]
    left_shoulder = lm[11]

    wrist_motion = abs(left_wrist.y - right_wrist.y)
    hand_above_shoulder = left_wrist.y < left_shoulder.y

    return {
        "wrist_motion": wrist_motion,
        "hand_above_shoulder": hand_above_shoulder
    }