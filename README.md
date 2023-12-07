# Checkbox-Sorter

## Case Study: Sorting Checkbox Data from Google Sheets Responses

This code demonstrates how to sort checkbox data from responses in Google Sheets. It addresses a common challenge faced by users who want to analyze data collected through Google Forms, where users can select multiple options from a list of checkboxes.

### Prerequisites

- Python 3.x
- `csv` module
- Google Sheets access and permission to edit the target spreadsheet

### Scripts

The following Python scripts are used in this case study:

1. **groups.py** This script reads data from a CSV file containing meeting options and associated names. It then outputs a the names in a column, and chosen meeting options beside enclosed in a list
2. **script.py:** This script writes grouped meeting options and associated names to a text file for further analysis or presentation.

### Example Inputs

**meeting_options.csv:**

| Name                     | Chosen Meeting Options                                                                                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| John Doe                 | Friday, 22nd (offline), Saturday, 23rd (offline)                                                                                                                        |
| Jane Doe                 | Monday, 11th (online), Tuesday, 12th (offline)                                                                                                                          |
| Eghosa-Osahon Marvellous | Monday, 11th (online), Tuesday, 12th (offline), Friday, 15th (offline), Saturday, 16th (online), Monday, 18th (offline), Tuesday, 19th (online), Friday, 22nd (offline) |

**Note:** This is an example file, and the actual data in your CSV file may differ.

### Example Outputs

`grouped_meeting_options.txt:`

**Meeting Option:** Monday, 11th (online)

- Jane Doe
- Eghosa-Osahon Marvellous

**Meeting Option:** Tuesday, 12th (offline)

- Jane Doe
- Eghosa-Osahon Marvellous

**Meeting Option:** Friday, 15th (offline)

- Eghosa-Osahon Marvellous

**Meeting Option:** Saturday, 16th (online)

- Eghosa-Osahon Marvellous

**Meeting Option:** Monday, 18th (offline)

- Eghosa-Osahon Marvellous

**Meeting Option:** Tuesday, 19th (online)

- Eghosa-Osahon Marvellous

**Meeting Option:** Friday, 22nd (offline)

- John Doe
- Eghosa-Osahon Marvellous

**Note:** This is an example output, and the actual data in your text file may differ depending on the content of your CSV file.

### Adapting for Different Requirements

This code can be adapted to accommodate different requirements:

- **Different meeting option format:** If your meeting options are formatted differently, you can modify the `groups.py` script to handle the specific format.
- **Multiple selection types:** If your Google Form allows multiple selection types, you can modify the code to handle various data formats accordingly.
- **Different output format:** You can modify the `script.py` script to output the data in a different format, such as a JSON file or a spreadsheet.

### Conclusion

This case study demonstrates how to sort and group checkbox data from Google Sheets responses. The included scripts can be easily adapted to meet specific requirements and provide a valuable tool for analyzing data collected through Google Forms.
