import random
import math
import numpy as np
import pandas as pd


def generate_data(n_students=10):
    records = []
    student_ids = random.sample(range(1001, 9999), n_students)

    for sid in student_ids:
        marks      = round(random.uniform(0, 100), 2)
        attendance = round(random.uniform(0, 100), 2)
        assignment = round(random.uniform(0, 50),  2)
        records.append((sid, marks, attendance, assignment))

    return records


def classify_students(df):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for i in range(len(df)):
        sid = df["student_id"][i]
        m   = df["marks"][i]
        att = df["attendance_percentage"][i]

        if m < 40 or att < 50:
            categories["At Risk"].append(sid)
        elif m > 90 and att > 80:
            categories["Top Performer"].append(sid)
        elif 71 <= m <= 90:
            categories["Good"].append(sid)
        else:
            categories["Average"].append(sid)

    return categories


def analyze_data(df):
    marks_arr = np.array(df["marks"])

    mean_marks   = float(np.sum(marks_arr) / len(marks_arr))
    median_marks = float(np.median(marks_arr))
    std_dev      = float(math.sqrt(np.sum((marks_arr - mean_marks)**2) / len(marks_arr)))
    max_marks    = float(np.max(marks_arr))
    min_marks    = float(np.min(marks_arr))

    correlation = float(np.corrcoef(df["marks"], df["attendance_percentage"])[0, 1])

    denominator = max_marks - min_marks if max_marks != min_marks else 1
    df["normalized_marks"] = (marks_arr - min_marks) / denominator

    # Updated performance index
    df["performance_index"] = (
        df["normalized_marks"] * 0.5 +
        (df["assignment_score"] / 50) * 0.3 +
        (df["attendance_percentage"] / 100) * 0.2
    )

    summary_tuple = (
        round(mean_marks, 2),
        round(std_dev, 2),
        round(max_marks, 2)
    )

    stats = {
        "mean_marks": round(mean_marks, 2),
        "median_marks": round(median_marks, 2),
        "std_dev": round(std_dev, 2),
        "max_marks": round(max_marks, 2),
        "min_marks": round(min_marks, 2),
        "correlation": round(correlation, 4),
    }

    return summary_tuple, stats


def detect_patterns(categories, stats):
    std_dev       = stats["std_dev"]
    at_risk_count = len(categories["At Risk"])
    top_count     = len(categories["Top Performer"])

    if std_dev < 15 and at_risk_count <= 3 and top_count >= 2:
        return "Stable Academic System"
    elif at_risk_count > 5 or std_dev > 25:
        return "Critical Attention Required"
    else:
        return "Moderate Performance"


# ---------------- MAIN ----------------

n_students = 10

records = generate_data(n_students)
df = pd.DataFrame(records, columns=[
    "student_id", "marks", "attendance_percentage", "assignment_score"
])

categories = classify_students(df)
summary, stats = analyze_data(df)
system_label = detect_patterns(categories, stats)

print("\nSTUDENT DATA:")
print(df)

print("\nCATEGORIES:")
print(categories)

print("\nSTATISTICS:")
print(stats)

print("\nFINAL SYSTEM INSIGHT:")
print(system_label)