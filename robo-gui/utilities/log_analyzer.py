"""Module to analyse the log file """
import re


def analyse_log(log_file_path):
    """Analyse the log file and print the results"""
    with open(log_file_path, "r", encoding="utf-8") as file:
        log_content = file.read()

    # Define a regular expression pattern to extract relevant information
    pattern = re.compile(
        r"Quelle = (\w+)\n\s+Ziel : (\w+).*?Dateien:.*?(\d+)\s+(\d+)",
        re.DOTALL,
    )

    # Initialize a dictionary to store the counts for each source-destination combination
    copy_counts = {}

    # Find all matches in the log content
    matches = re.finditer(pattern, log_content)

    result = []

    # Iterate through the matches and update the counts in the dictionary
    for match in matches:
        source = match.group(1)
        destination = match.group(2)
        total_files = int(match.group(3))  # Total files
        copied_files = int(match.group(4))  # Copied files

        # Combine source and destination into a tuple
        source_destination = (source, destination)

        # Update the counts in the dictionary
        if source_destination in copy_counts:
            copy_counts[source_destination] += copied_files
        else:
            copy_counts[source_destination] = copied_files

    # Print the results
    for (source, destination), count in copy_counts.items():
        result.append([source, destination, count])

    print(result)
