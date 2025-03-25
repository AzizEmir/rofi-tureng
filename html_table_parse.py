import sys
from bs4 import BeautifulSoup
from tabulate import tabulate

# Check if the HTML file path is passed as an argument
if len(sys.argv) != 2:
    print("Usage: python3 main.py <HTML_FILE_PATH>")
    sys.exit(1)

# Get the HTML file path from the command-line argument
html_file_path = sys.argv[1]

# Read the content of the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")
rows = []

# Extract the rows from the table
table_rows = soup.select('tr[class^="tureng-manual-stripe"]')

# Loop through each row and extract the columns
for row in table_rows:
    columns = row.find_all('td')
    if len(columns) >= 4:
        # Extract the relevant columns: No, Kategori, Türkçe, İngilizce
        no = columns[0].text.strip() if columns[0].text.strip() != '' else '-'
        kategori = columns[1].text.strip()
        turkce = columns[2].text.strip()
        ingilizce = columns[3].text.strip()

        # Remove "i." if it appears in the "İngilizce" column
        ingilizce = ingilizce.replace("i.", "").strip()

        rows.append([no, kategori, turkce, ingilizce])

# Define the table headers
headers = ["No", "Kategori", "Türkçe", "İngilizce"]

# Print the table in a readable format
print(tabulate(rows, headers, tablefmt="grid"))
