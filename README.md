# Multi-Dimensional Academic Intelligence System

## Overview
This project analyzes student performance using multiple factors such as marks, attendance, and assignment scores. It combines all these parameters to provide meaningful academic insights instead of relying only on marks.

The system is implemented using Python with NumPy and Pandas.

---

## Objective
- Analyze student performance using multiple dimensions  
- Apply statistical techniques  
- Classify students into categories  
- Detect patterns and generate final insights  

---

## Personalization Applied
- Last digit of Register Number = **X**  
- Number of students generated = **X+10**  

This ensures the dataset is unique for each student.

---

## System Workflow

### 1. Data Generation
Student data is generated using the random module.

---

### 2. Classification
- Marks < 40 OR Attendance < 50 → At Risk  
- Marks 40–70 → Average  
- Marks 71–90 → Good  
- Marks > 90 AND Attendance > 80 → Top Performer  

---

### 3. Statistical Analysis
- Mean  
- Median  
- Standard Deviation  
- Correlation  

---

### 4. Performance Index
performance_index = (
    normalized_marks * 0.5 +
    (assignment_score / 50) * 0.3 +
    (attendance_percentage / 100) * 0.2
)

---
### 5. Pattern Detection
The system analyzes the computed statistics and classified data to identify important patterns in student performance. 

- **Consistency Check:**  
  If the standard deviation is less than 15, it indicates that student performance is consistent. Otherwise, it shows high variation.

- **Attendance Risk:**  
  If more than 3 students fall under the "At Risk" category, it indicates a potential attendance issue.

- **High Achievement:**  
  If there are at least 2 students in the "Top Performer" category, it reflects strong academic performance.

These patterns help in understanding the overall behavior of the student dataset.

---

### 6. Final System Insight
Based on the detected patterns, the system generates an overall evaluation of academic performance:

- **Stable Academic System:**  
  When performance is consistent, risk is low, and there are enough top performers.

- **Moderate Performance:**  
  When conditions are average and do not strongly indicate stability or critical issues.

- **Critical Attention Required:**  
  When there are many at-risk students or high variation in marks.

This final insight provides a clear summary of the academic system's overall condition.
