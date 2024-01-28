import pandas as pd
import numpy as np

# Create empty lists to store user input data
appliance_names = []
kwh_usage = []
due_dates = []

# Prompt the user to enter the number of appliances
num_appliances = int(input("Enter the number of appliances: "))

# Loop to collect data for each appliance
for i in range(num_appliances):
    appliance_name = input(f"Enter the name of appliance {i + 1}: ")
    usage = float(input(f"Enter the kWh usage for {appliance_name}: "))
    due_date = input(f"Enter the due date for {appliance_name} (DD/MM): ")

    appliance_names.append(appliance_name)
    kwh_usage.append(usage)
    due_dates.append(due_date)

# Create a pandas DataFrame
data = {
    'Appliance Name': appliance_names,
    'kWh Usage': kwh_usage,
    'Due Date': due_dates
}
df = pd.DataFrame(data)

# Display the DataFrame
print("\nElectricity Usage Information:")
print(df)

# Use numpy to find the maximum and minimum kWh usage
max_usage = np.max(kwh_usage)
min_usage = np.min(kwh_usage)

print(f"\nMaximum kWh Usage: {max_usage:.2f} kWh")
print(f"Minimum kWh Usage: {min_usage:.2f} kWh")

# Save the DataFrame to a CSV file
csv_filename = 'electricity_usage_data.csv'
df.to_csv(csv_filename, index=False)
print(f"Data saved to {csv_filename}")