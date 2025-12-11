import sys
import cloudscraper
from bs4 import BeautifulSoup
import subprocess
import os

# URL parametresini al
url = sys.argv[1]

# Optimized configuration for v3 challenges
scraper = cloudscraper.create_scraper(
    interpreter='js2py',  # Recommended for v3 challenges
    delay=5,              # Allow more time for complex challenges
    debug=False            # Enable debug output to see v3 detection
)

# Send the request to the URL
response = scraper.get(url)

# Check if the response is successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all <table> tags (not just the first one)
    tables = soup.find_all("table")

    if tables:
        # Get the current directory where this script is located
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Define the relative file path for the output
        output_file_path = os.path.join(current_dir, "output.html")

        # Open the output file to write
        with open(output_file_path, "w", encoding="utf-8") as file:
            for table in tables:
                # Remove unwanted <tr> rows and <i> tags in the tables
                for row in table.find_all("tr", class_="example-sentences-row"):
                    row.decompose()
                for row in table.find_all("i", class_=""):
                    row.decompose()

                # Write the prettified HTML for each table to the file
                file.write(table.prettify())

        print(f"Output saved to {output_file_path}")

        # Define the relative file path for the script to run
        script_path = os.path.join(current_dir, "html_table_parse.py")

        # Run the html_table_parse.py script with the output.html as argument and capture its output
        with open(os.path.join(current_dir, "script_output.txt"), "w", encoding="utf-8") as output_file:
            subprocess.run(["python3", script_path, output_file_path], stdout=output_file, stderr=subprocess.PIPE)
    else:
        print("No <table> found.")
else:
    print(f"Error: {response.status_code}")
