import pandas as pd

def load_and_clean_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)

    # Handling Missing Values: Fill with median or drop rows/columns based on the context
    # For demonstration, we'll fill missing values with the median of each column
    data = data.fillna(data.median())

    # Removing Unnecessary Columns: Dropping 'Unnamed: 0' if it exists
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])

    # Outlier Detection and Handling: Using IQR for demonstration on one of the 'em_' columns
    # Calculate Q1, Q3, and IQR
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1

    # Assuming 'em_60000' is the column for outlier detection
    # Remove outliers from 'em_60000'
    data = data[~((data['em_60000'] < (Q1['em_60000'] - 1.5 * IQR['em_60000'])) |
                  (data['em_60000'] > (Q3['em_60000'] + 1.5 * IQR['em_60000'])))]

    return data
