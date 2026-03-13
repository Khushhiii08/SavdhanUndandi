# 🛡️ SavdhanUndandi – Preventive AI for Public Safety

**SavdhanUndandi** is a real-time **preventive surveillance intelligence system** that identifies *early-stage behavioral risk* in public spaces **before incidents escalate**.

Unlike reactive systems that detect violence after it occurs, SavdhanUndandi focuses on **contextual, explainable, and ethical prevention**, making it suitable for real-world deployment and edge devices.

---

## 🚨 Problem Statement

Traditional CCTV systems are largely **passive and reactive**:

- Incidents are detected **after harm occurs**
- Continuous human monitoring is required
- High false positives in dynamic environments (sports, crowds, play)
- Heavy dependence on cloud and GPU-based systems

There is a need for a **lightweight, deployable, and explainable AI system** that can identify **early warning signals** while minimizing false alarms.

---

## 💡 Our Solution

SavdhanUndandi uses a **multi-signal preventive AI pipeline** that evaluates:

- 👤 Human presence (YOLO-based person detection)
- 🦴 Body posture and movement (MediaPipe Pose)
- 🕒 Dwell time and loitering behavior
- 👥 Crowd density
- 🏃 Motion dynamics
- ⚖️ Context-aware dampening (e.g., sports and play scenarios)

Instead of classifying actions as “violent” or “non-violent”, the system assigns a **continuous risk score (0.0 – 1.0)** and raises **preventive alerts only when necessary**.

---

## 🧠 Key Design Philosophy

- **Prevention over reaction**
- **Explainable rule-based logic**
- **Low false positives**
- **Ethical and bias-aware**
- **Edge-friendly**

---

## 🏗️ System Architecture

Video Stream (CCTV / Dataset)

↓

YOLOv8 – Person Detection

↓

MediaPipe Pose – Body Language Analysis

↓

Behavior Logic Engine
(Motion + Crowd + Dwell + Context)

↓

Continuous Risk Score

↓

Preventive Alert System

---

## 🔍 Why Only Normal Videos?

This prototype is intentionally designed to operate on **normal activity footage**.

- The goal is **early risk detection**, not violence recognition
- Abnormal events are **not required** to demonstrate prevention
- Sports and playful activities are correctly identified as **low-risk**
- Reduces ethical concerns and dataset bias

This aligns with real-world deployment where **prevention must occur before escalation**.

---

## 📊 Risk Scoring Behavior (Examples)

| Scenario | Typical Risk |
|--------|-------------|
| Empty corridor | 0.00 – 0.05 |
| Walking individuals | 0.05 – 0.15 |
| Standing group | 0.15 – 0.30 |
| Kids playing basketball | 0.20 – 0.35 |
| Heated argument (early stage) | 0.45 – 0.65 |
| Escalation indicators | 0.70+ |

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **YOLOv8 (pretrained)**
- **MediaPipe Pose**
- **Rule-based behavior logic**
- **GitHub for version control**

---

## ▶️ How to Run

1. Install dependencies
   ```bash
   pip install opencv-python mediapipe ultralytics
   ```
2.	Place a sample video in:
   ```bash
  	data/videos/
```
4.	Update VIDEO_SOURCE in config.py
5.	Run the system:
   ```bash
   python main.py
```
Press Q to exit.

---

⚠️ Ethical Considerations
- No facial recognition
- No identity storage
- No personal profiling
- Risk is contextual and temporary
- Designed to assist humans, not replace judgment

---

🚀 Hackathon Alignment (AMD Slingshot)
- Lightweight inference
- No dependency on CUDA
- Edge-deployable architecture
- Modular and extensible design
- Focus on real-world impact

---

📌 Future Enhancements
- Restricted-zone monitoring
- Temporal anomaly learning
- Multi-camera correlation
- Dashboard and analytics UI
- Edge optimization on AMD hardware

---

👥 Team & Acknowledgment

Built as a preventive AI prototype for the AMD Slingshot Hackathon with a focus on safety, ethics, and deployability.

---

“High activity does not imply high threat — context defines risk.”
