import PyPDF2
import os
import csv

from pdfminer.high_level import extract_text

def extract_text_after_keywords(pdf_path, keywords):
    # Extract text from the PDF file
    text = extract_text(pdf_path)
    # Initialize an empty list to store extracted lines
    extracted_lines = []
    # Flag to track if any keyword has been found
    found_keyword = False
    cnt=0
    # Iterate through each line in the extracted text
    for line in text.split('\n'):
        # Check for each keyword in the line
        for keyword in keywords:
            if keyword in line:
                # Set the flag to True once any keyword is found
                found_keyword = True
                break
        # If any keyword is found, add the line to the list
        if found_keyword:
            extracted_lines.append(line.strip())
            cnt+=1
            if cnt==10:
                cnt=0
                break
            # Break the loop to stop searching subsequent lines
    # If no keyword is found, return None
    if not found_keyword:
        return None
    # Return the first 10 lines after the occurrence of any keyword
    return extracted_lines[:10]
lst=["properties","specifications","characteristics","Properties","Specifications","Characteristics","Features"]
def traverse_directory(directory):
    arr=[]
    cnt=0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):  # Filter HTML files
                file_path = os.path.join(root, file)
                x=extract_text_after_keywords(file_path,lst)
                #print(x)
                print(file_path)
                if x!=None:
                    arr.append(("datasheets/"+file,x))
                    #print(file_path)
    return arr
# Example usage
pdf_path = r"C:/Users/Traian/Downloads/lenntech-selection-suez/lenntech-suez/data-sheets/SUEZ-BetzDearborn-AE1700-L.pdf"  # Path to your PDF file
keyword = ["properties"]  # Keyword to search for
#print(extract_text_after_keywords(pdf_path, keyword))
directory = r'C:\Users\Traian\Downloads\lenntech-data-sheets\data-sheets'

arr=traverse_directory(directory)
csv_file_path = "products.csv"

# Write the array to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Define the CSV writer and specify the column names
    writer = csv.DictWriter(csvfile, fieldnames=["path", "string"])

    # Write the header
    writer.writeheader()

    # Write each tuple as a row in the CSV file
    for path, string in arr:
        writer.writerow({"path": path, "string": string})

print("CSV file has been created successfully!")
print(len(arr))