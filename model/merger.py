import csv
with open('products.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    data=[]
    # Iterate over each row in the CSV file
    for row in reader:
        # Remove any characters that cannot be decoded
        cleaned_row = [cell.encode('utf-8', 'ignore').decode('utf-8', 'ignore') for cell in row]
        # Assuming each row has two columns, create a tuple with the values and append it to the list
        if len(cleaned_row) == 2:  # Ensure each row has exactly two columns
            data.append((cleaned_row[0], cleaned_row[1]))
    newdata=[]
    for (path, description) in data:
        newdata.append((path,''.join([s.rstrip(',') for s in description]).strip('[]')))
    csv_file_path = "products.csv"

# Write the array to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Define the CSV writer and specify the column names
    writer = csv.DictWriter(csvfile, fieldnames=["path", "string"])

    # Write the header
    writer.writeheader()

    # Write each tuple as a row in the CSV file
    for path, string in newdata:
        writer.writerow({"path": path, "string": string})