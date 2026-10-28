"""Student performance data preprocessing practical."""
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).with_name("student_performance.csv")

def main():
    df = pd.read_csv(DATA_PATH)
    print("Raw dataset shape:", df.shape)
    print("\nMissing values before cleaning:\n", df.isna().sum())

    # Remove exact duplicate records
    df = df.drop_duplicates().copy()

    # Impute missing values
    for col in ["Age", "Study_Hours", "Attendance"]:
        df[col] = df[col].fillna(df[col].median())
    df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

    # Select relevant columns; exclude identifier and City for this example
    selected = df[
        ["Age", "Gender", "Study_Hours", "Attendance",
         "Internet_Access", "Final_Score"]
    ].copy()

    # One-hot encode categorical variables
    encoded = pd.get_dummies(
        selected,
        columns=["Gender", "Internet_Access"],
        drop_first=True,
        dtype=int,
    )

    # Min-Max normalize input features only; keep Final_Score interpretable
    for col in ["Age", "Study_Hours", "Attendance"]:
        minimum, maximum = encoded[col].min(), encoded[col].max()
        if maximum != minimum:
            encoded[col] = (encoded[col] - minimum) / (maximum - minimum)

    output_path = Path(__file__).with_name("student_performance_cleaned.csv")
    encoded.to_csv(output_path, index=False)

    print("\nCleaned dataset shape:", encoded.shape)
    print("\nMissing values after cleaning:\n", encoded.isna().sum())
    print("\nDescriptive statistics:\n", df[["Age", "Study_Hours", "Attendance", "Final_Score"]].describe())
    print("\nCorrelation matrix:\n", df[["Study_Hours", "Attendance", "Final_Score"]].corr())
    print(f"\nSaved processed data to: {output_path.name}")

if __name__ == "__main__":
    main()
