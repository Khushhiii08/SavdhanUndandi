import csv
import datetime

LOG_FILE = "logs/events.csv"

def log_event(event, score):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), event, score])

def raise_alert(event, score):
    print(f"🚨 {event} | Risk Score: {score}")
    log_event(event, score)