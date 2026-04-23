# Multi-Dimensional Academic Intelligence System

## Overview
This project is about analyzing student performance using multiple factors like marks, attendance, and assignment scores. Instead of just looking at marks, the system considers all these factors together to give better insights into student performance.

The program uses Python along with NumPy and Pandas for handling data and calculations.

---

## What this project does
- Generates student data using random values  
- Stores data using lists, tuples, and dictionaries  
- Converts the data into a Pandas DataFrame  
- Classifies students into categories like:
  - At Risk
  - Average
  - Good
  - Top Performer  
- Calculates statistics such as mean, median, and standard deviation  
- Finds the relationship between marks and attendance  
- Creates a performance index for each student  
- Detects patterns and gives a final system insight  

---

## Data Format
Each student record contains:
(student_id, marks, attendance_percentage, assignment_score)

---

## How it works (simple steps)
1. Generate student data  
2. Store it in a list  
3. Convert it into a DataFrame  
4. Classify students based on conditions  
5. Perform statistical analysis  
6. Detect patterns and generate final output  

---

## Performance Index
I used a custom formula:
```python
performance_index = (
    normalized_marks * 0.5 +
    (assignment_score / 50) * 0.3 +
    (attendance_percentage / 100) * 0.2
)
