import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("hospital_data.csv")
    cost_series = df['bill']
    date_series = df['admission_date']
    
    print("\n original bill series:")
    print(cost_series)
    
    print("\n original data series:")
    print(date_series)

    # user input for cleaning and plotting 
    print("\n fill the missing bill value with median before plotting?(yes/no):")
    fill_confirm = input().strip().lower()
    print("convert admission date to DD/MM/YYYY for display? (yes/no)")
    date_format_confirm = input().strip().lower()

    # perform clean bill missing values
    if fill_confirm == 'yes':
        median_cost = cost_series.median()
        cleaned_cost_series = cost_series.fillna(median_cost)
        print(cleaned_cost_series)
    else:
        print("\n no changes to medical cost.")
        cleaned_cost_series = cost_series  # Ensure variable is always defined

    # ✅ Corrected: Match actual date format in CSV (DD-MM-YYYY)
    cleaned_date_series = pd.to_datetime(date_series, format='%d-%m-%Y', errors='coerce')

    if date_format_confirm == 'yes':
        display_dates = cleaned_date_series.dt.strftime('%d-%m-%Y')
    else:
        display_dates = cleaned_date_series

    # Debug print
    print("\nCleaned Dates:")
    print(cleaned_date_series.head())
    print("Cleaned Bills:")
    print(cleaned_cost_series.head())

    # plot
    plt.figure(figsize=(10, 10))
    plt.plot(cleaned_date_series, cleaned_cost_series, marker='o', ls='-', color='blue')
    plt.title("Medical cost over admissions dates")
    plt.xlabel("admission_date")
    plt.ylabel("medical_cost ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # update AND save
    if fill_confirm == 'yes' or date_format_confirm == 'yes':
        df['bill'] = cleaned_cost_series
        df['admission_date'] = display_dates if date_format_confirm == 'yes' else cleaned_date_series
        df.to_csv("hospital_data.csv", index=False)
        print("\n updated csv saved to 'hospital_data.csv'.")
    else:
        print("\n not updated")

except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")
except ValueError as e:
    print(f"error: invalid date format ({e}).")
