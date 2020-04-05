"""
Daily updates on the spread of COVID-19 in Sweden.

Datasets grouped by different categories. The datasets contain information in Swedish.
Categories

    Time series of infected people.
    Time series of deceased people.
    Time series of pople getting intensive care.
    Grouped by region.
    Grouped by age.
    Grouped by gender.
"""
publisher = "The Public Health Agency of Sweden"

# Datasets on the spread of COVID-19 from The Public Health Agency of Sweden.
files = {
    'infected':
        'https://www.the-data-smorgasbord.com/outbreak/swe-public-health-agency/time_series.csv',
    'intensive_care':
        'https://www.the-data-smorgasbord.com/outbreak/swe-public-health-agency/intensive_care_time_series.csv',
    'deceased':
        'https://www.the-data-smorgasbord.com/outbreak/swe-public-health-agency/deceased_time_series.csv',
}
