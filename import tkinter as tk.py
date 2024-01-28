import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np

kwh_usage = []
# Function to calculate and display the total and average kWh usage
def calculate_usage():
    appliance_names = []
    kwh_usage = []

    for i in range(num_appliances.get()):
        appliance_name = appliance_entries[i].get()
        usage = float(usage_entries[i].get())

        appliance_names.append(appliance_name)
        kwh_usage.append(usage)

    data = {
        'Appliance Name': appliance_names,
        'kWh Usage': kwh_usage,
    }
    df = pd.DataFrame(data)

    result_label.config(text="Calculating...")

    # Use numpy to find the sum and average of kWh usage
    total_usage = np.sum(kwh_usage)
    average_usage = np.mean(kwh_usage)

    result_label.config(text=f"Total kWh Usage: {total_usage:.2f} kWh\nAverage kWh Usage: {average_usage:.2f} kWh")

# Create the main window
root = tk.Tk()
root.title("Electricity Usage Calculator")

# Label and entry for the number of appliances
num_appliances_label = tk.Label(root, text="Enter the number of appliances:")
num_appliances_label.pack()
num_appliances = tk.IntVar()
num_appliances_entry = tk.Entry(root, textvariable=num_appliances)
num_appliances_entry.pack()

# Button to confirm the number of appliances
num_appliances_button = tk.Button(root, text="Confirm", command=calculate_usage)
num_appliances_button.pack()

appliance_entries = []
usage_entries = []
due_entries = []

# Function to create input fields for appliances
def create_input_fields():
    for i in range(num_appliances.get()):
        appliance_label = tk.Label(root, text=f"Enter the name of appliance {i + 1}:")
        appliance_label.pack()
        appliance_entry = tk.Entry(root)
        appliance_entry.pack()
        appliance_entries.append(appliance_entry)

        usage_label = tk.Label(root, text=f"Enter the kWh usage for appliance {i + 1}:")
        usage_label.pack()
        usage_entry = tk.Entry(root)
        usage_entry.pack()
        usage_entries.append(usage_entry)

    num_appliances_button.config(state=tk.DISABLED)
    create_fields_button.config(state=tk.DISABLED)
    calculate_button.config(state=tk.NORMAL)

# Button to create input fields for appliances
create_fields_button = tk.Button(root, text="Create Input Fields", command=create_input_fields)
create_fields_button.pack()

# Button to calculate usage (initially disabled)
calculate_button = tk.Button(root, text="Calculate Usage", command=calculate_usage, state=tk.DISABLED)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Function to provide recommendations for minimizing appliance usage
def provide_recommendations():
    recommendations = []
    for usage in kwh_usage:
        if usage > average_usage:
            recommendations.append("Consider reducing usage.")
        else:
            recommendations.append("Usage is within an acceptable range.")
    
# Create a button to provide recommendations
recommendations_button = tk.Button(root, text="Provide Recommendations", command=provide_recommendations)
recommendations_button.pack()

root.mainloop()
