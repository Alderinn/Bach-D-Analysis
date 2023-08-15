import csv

# Specify the input CSV file and output CSV file
input_file = 'results.csv'
output_file = 'results(fixed).csv'
def fixMyBrokenCSV():
    # Open the input CSV file for reading and output CSV file for writing
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        # Write the header row to the output file
        header = next(csv_reader)
        csv_writer.writerow(header)

        # Iterate through the rows in the input CSV
        for row in csv_reader:
            # Check if the row has all three values (season, episode, and count)
            if len(row) == 3:
                csv_writer.writerow(row)

    print("Filtered CSV file created successfully.")