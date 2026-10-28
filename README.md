# Machine Learning with Python: Data Preprocessing

A beginner-friendly practical project demonstrating data loading, inspection, duplicate removal, missing-value imputation, feature selection, one-hot encoding, Min-Max normalization, and exploratory data analysis (EDA) on a sample student-performance dataset.

## Project files

- `student_performance.csv` — raw sample dataset, including missing values and an exact duplicate row.
- `preprocessing.py` — complete preprocessing workflow.
- `requirements.txt` — Python dependency list.
- `student_performance_cleaned.csv` — generated when the script runs.
- `Machine_Learning_Preprocessing_Report.docx` — written practical report (if you add the report file).

## Requirements

- Python 3.9+
- pandas

Install the dependency:

```bash
pip install -r requirements.txt
```

## Run the project

Keep `preprocessing.py` and `student_performance.csv` in the same folder, then run:

```bash
python preprocessing.py
```

The script prints data-quality checks, descriptive statistics, and correlations. It also creates `student_performance_cleaned.csv`.

## Workflow

1. Load the CSV into a Pandas DataFrame.
2. Inspect dimensions, missing values, and summary statistics.
3. Remove exact duplicate rows.
4. Fill missing numeric values with their median and missing `Gender` values with the mode.
5. Exclude `Student_ID` and `City` from the modelling example.
6. One-hot encode `Gender` and `Internet_Access`.
7. Min-Max normalize `Age`, `Study_Hours`, and `Attendance` to the 0–1 range.
8. Explore descriptive statistics and correlations.

## Important note

This is a small illustrative dataset, not a validated predictive model. Correlations in this sample do not establish causation. For a real predictive model, split the data into training and test sets and fit preprocessing steps on training data only to avoid data leakage.

## Author

Sourabh  
Course: Machine Learning using Python
