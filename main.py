# src/production_code.py
from data_cleaning import load_and_clean_data
from insights_visualization import plot_emission_trends

def main():
    # Load and clean the dataset
    cleaned_df = load_and_clean_data('data/sample_data_100.csv')

    # Plot emission trends
    plot_emission_trends(cleaned_df)

if __name__ == "__main__":
    main()
