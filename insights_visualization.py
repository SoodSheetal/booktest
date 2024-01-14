# src/insights_visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_emission_trends(df):
    # Plotting emissions data over the years
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=df, x='year', y='em_60000', label='Scope 1 CO2e emissions')
    sns.lineplot(data=df, x='year', y='em_60100', label='Scope 2 CO2e emissions (location based)')
    sns.lineplot(data=df, x='year', y='em_60200', label='Scope 2 CO2e emissions (market based)')
    sns.lineplot(data=df, x='year', y='em_60300', label='Scope 3 CO2e emissions (total)')
    plt.title('Emissions Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Emissions (tCO2e)')
    plt.legend()
    plt.show()

    # ... Add more visualization functions as needed
