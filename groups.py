import csv

# Define the filename
filename = "responses.csv"

# Create empty lists for names and chosen meeting options
names = []
chosen_meeting_options = []

# Open the CSV file
with open(filename, "r") as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)

    # Extract names and chosen meeting options from each row
    for row in reader:
        names.append(row["Name"])
        chosen_meeting_options.append(row["Meeting Days"].split("), "))

# Create a list of dictionaries with names and chosen meeting options
combined_data = []
for i in range(len(names)):
    combined_data.append(
        {"Name": names[i], "Chosen Meeting Options": chosen_meeting_options[i]}
    )

# Print the results
print("Names and chosen meeting options:")
for item in combined_data:
    print(f"Meeting Options: {item['Chosen Meeting Options']}")

# Save the results to a new CSV file named "meeting_options.csv"
with open("meeting_options.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Name", "Chosen Meeting Options"])
    writer.writeheader()
    writer.writerows(combined_data)

print("The results have also been saved to a file named 'meeting_options.csv'.")
