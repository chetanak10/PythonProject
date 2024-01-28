import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from the CSV file
csv_filename = 'electricity_usage_data.csv'
df = pd.read_csv(csv_filename)

# Extract appliance names and kWh usage from the DataFrame
appliances = df['Appliance Name']
kwh_usage = df['kWh Usage']

# Create an array of indices for the appliances
appliance_indices = np.arange(len(appliances))

# Create the bar graph
plt.figure(figsize=(10, 6))
plt.bar(appliance_indices, kwh_usage, align='center')

# Set the appliance names as x-axis labels
plt.xticks(appliance_indices, appliances, rotation=15)

# Label the axes and give the plot a title
plt.xlabel('Appliances')
plt.ylabel('kWh Usage')
plt.title('Electricity Usage by Appliances')

# Show the bar graph
plt.tight_layout()
plt.show()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(kwh_usage, labels=appliances, autopct='%1.1f%%', startangle=140)

# Set the aspect ratio to be equal so that the pie chart is circular
plt.axis('equal')

# Add a title
plt.title('Electricity Usage by Appliances (Pie Chart)')

# Show the pie chart
plt.show()