import csv
from statistics import mean

def read_rehab_log(file_path):
    rows = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def summarize(rows):
    if not rows:
        print("No data found.")
        return

    breathing_sessions = []
    walking_minutes = []
    dyspnea_scores = []
    fatigue_scores = []

    for row in rows:
        b = safe_float(row.get("breathing_exercise_sessions"))
        w = safe_float(row.get("walking_minutes"))
        d = safe_float(row.get("dyspnea_score"))
        f = safe_float(row.get("fatigue_score"))

        if b is not None:
            breathing_sessions.append(b)
        if w is not None:
            walking_minutes.append(w)
        if d is not None:
            dyspnea_scores.append(d)
        if f is not None:
            fatigue_scores.append(f)

    print("PulmoRehab Summary")
    print("------------------")
    print(f"Total entries: {len(rows)}")

    if breathing_sessions:
        print(f"Average breathing exercise sessions: {mean(breathing_sessions):.2f}")
    if walking_minutes:
        print(f"Average walking minutes: {mean(walking_minutes):.2f}")
    if dyspnea_scores:
        print(f"Average dyspnea score: {mean(dyspnea_scores):.2f}")
    if fatigue_scores:
        print(f"Average fatigue score: {mean(fatigue_scores):.2f}")

if __name__ == "__main__":
    file_path = "templates/rehab-daily-log.csv"
    data = read_rehab_log(file_path)
    summarize(data)
