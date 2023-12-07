import csv


def read_meeting_options_csv(filename):
    """
    Reads data from a CSV file containing meeting options and associated names.

    Args:
        filename: The path to the CSV file.

    Returns:
        A dictionary where keys are meeting options (strings) and values are lists of unique names (strings) associated with that option.
    """
    meeting_options = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"]
            raw_options = (
                row["Chosen Meeting Options"].lstrip("[").rstrip("]").split(", ")
            )
            options = []
            for option in raw_options:
                option = option.strip().strip("'").strip()
                if " " in option:
                    options.append(option)
                    meeting_options.setdefault(
                        option, set()
                    )  # Initialize set for unique names per option
            for option in options:
                if name not in meeting_options[option]:
                    meeting_options[option].add(name)  # Add unique names to the set
    return meeting_options


def write_grouped_data_to_text(data, filename):
    """
    Writes grouped meeting options and associated names to a text file.

    Args:
        data: A dictionary where keys are meeting options and values are sets of unique names.
        filename: The path to the text file.
    """
    with open(filename, "w") as textfile:
        for option, names in data.items():
            textfile.write(f"**Meeting Option:** {option}\n")
            for name in names:
                textfile.write(f"- {name}\n")


# Read data from the CSV file
grouped_meeting_options = read_meeting_options_csv("meeting_options.csv")

# Write grouped data to a text file
write_grouped_data_to_text(grouped_meeting_options, "grouped_meeting_options.txt")

print(
    "Grouped meeting options and completely unique names have been written to 'grouped_meeting_options.txt'."
)
