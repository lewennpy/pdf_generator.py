# Required Libraries:
# - fpdf: For generating PDFs
# - re: For regular expressions (used to remove non-ASCII characters)
#
# To install the necessary libraries, you can run the following commands:
# For Linux/macOS:
# pip install fpdf
#
# For Windows:
# python -m pip install fpdf
#
# Note: Make sure Python is installed on your system before running the script.

import os
import re
from fpdf import FPDF

# Function to remove emojis from the text
def remove_emojis(text):
    # Using regex to remove any non-ASCII characters
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Create the PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Content of the PDF
content = """
Here you can put the text that you want to add to the PDF.
This is an example of how the script will work.
If there is any text with emojis, they will be removed.
"""

# Remove emojis from the content (there may be some loss of other non-ASCII characters)
cleaned_content = remove_emojis(content)

# Add content to the PDF
pdf.multi_cell(0, 10, cleaned_content)  # 10 is a comfortable cell height for longer text

# Get the desktop path dynamically
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "Brandon_Morales_Gonzalez_Resume.pdf")

# Save the PDF to the desktop
pdf.output(file_path)

print(f"The PDF file has been saved to: {file_path}")

# End note
print("\nThank you for using this script!\n\nBest regards,\nLewenn\n\nFeel free to follow me on GitHub: https://github.com/lewennpy")
