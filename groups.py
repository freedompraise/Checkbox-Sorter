"""
This script sorts and groups names based on chosen meeting options from a CSV file.
"""

import csv

# Define the filename
FILENAME = "responses.csv"

# Create empty lists for names and chosen meeting options
names = []
chosen_meeting_options = []

# Open the CSV file with explicit encoding
with open(FILENAME, "r", encoding="utf-8") as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)

    # Extract names and chosen meeting options from each row
    for row in reader:
        names.append(row["Name"])
        chosen_meeting_options.append(row["Meeting Days"].split("), "))

# Create a list of dictionaries with names and chosen meeting options
combined_data = []
for index, name in enumerate(names):
    combined_data.append(
        {"Name": name, "Chosen Meeting Options": chosen_meeting_options[index]}
    )

# Print the results
print("Meeting Options:")

# Save the results to a new CSV file named "meeting_options.csv"
with open("meeting_options.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Name", "Chosen Meeting Options"])
    writer.writeheader()
    writer.writerows(combined_data)

print("The results have also been saved to a file named 'meeting_options.csv'.")
