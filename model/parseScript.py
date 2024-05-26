from bs4 import BeautifulSoup
import os
import csv

def get_text_between_words(input_string, start_word, end_word):
    start_index = input_string.find(start_word)
    if start_index == -1:
        return None  # Start word not found
    start_index += len(start_word)

    end_index = input_string.find(end_word, start_index)
    if end_index == -1:
        return None  # End word not found

    return input_string[start_index:end_index]
# Read the HTML file
def get_out_of_html(path):
    with open(path, 'r', encoding='utf-8',errors='ignore') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text from the parsed HTML
    text = soup.get_text()
    if "Specifications" not in text:
        return "not found"
    ans=""
    # Print or use the extracted text
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text()
        ans+=title+" "

    result = get_text_between_words(text, "Specifications", "Dimensions")
    if result:
        ans+=result+" "

    result = get_text_between_words(text, "Dimensions / Weights", "Download")
    if result:
        ans+=result
    return ans
def traverse_directory(directory):
    arr=[]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):  # Filter HTML files
                file_path = os.path.join(root, file)
                str=get_out_of_html(os.path.join(root, file))
                index = file_path.find("lenntech-selection-suez")
# Extract the substring starting from the index of "lennttech-selection-suez"
                if index != -1:  # Check if "lennttech-selection-suez" is found in the path
                    new_path = file_path[index:]
                    if str!="not found":
                         arr.append((new_path,str))
                         #print(str)
                         #print(str+" "+new_path)
    return arr

# Example usage:
directory = r'C:\Users\Traian\Downloads\lenntech-selection-suez\lenntech-suez\products'

arr=traverse_directory(directory)
csv_file_path = "productssuez.csv"

# Write the array to a CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    # Define the CSV writer and specify the column names
    writer = csv.DictWriter(csvfile, fieldnames=["path", "string"])

    # Write the header
    writer.writeheader()

    # Write each tuple as a row in the CSV file
    for path, string in arr:
        writer.writerow({"path": path, "string": string})

print("CSV file has been created successfully!")
print(len(arr))
