import pandas as pd


def group_by_meeting_options(filename, output_filename):
    """
    Groups the names of people under each of the meeting options from a CSV file and writes the results to a text file.

    Args:
      filename: The name of the CSV file.
      output_filename: The name of the text file to write the results to.
    """

    # Read the CSV file
    df = pd.read_csv(filename)

    # Create a dictionary to store the grouped data
    meeting_options_to_names = {}

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Get the meeting options
        meeting_options = row["Meeting Days"].split(", ")

        # Extract the day and presence from each option
        for option in meeting_options:
            try:
                day, presence = option.split(" (")
                presence = presence.strip(")")
            except ValueError:
                # Option doesn't have presence information
                day = option
                presence = "None"

            # Get the full meeting option
            meeting_option = f"{day} ({presence})"

            # Check if the meeting option exists in the dictionary
            if meeting_option not in meeting_options_to_names:
                meeting_options_to_names[meeting_option] = []

            # Add the name to the list for the corresponding meeting option
            meeting_options_to_names[meeting_option].append(row["Name"])

    # Open the text file for writing
    with open(output_filename, "w") as f:
        # Write the header line
        f.write("Meeting Option\tNames\n")

        # Write the grouped data to the file
        for meeting_option, names in meeting_options_to_names.items():
            f.write(f"{meeting_option}\t")
            for name in names:
                f.write(f"{name}, ")
            f.write("\n")


# Example usage
filename = "responses.csv"
output_filename = "grouped_meeting_options.txt"
group_by_meeting_options(filename, output_filename)

print(f"Grouped meeting options data written to '{output_filename}'.")
