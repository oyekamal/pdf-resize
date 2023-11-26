import PyPDF2
from reportlab.pdfgen import canvas

# Function to convert millimeters to points
def mm_to_points(mm):
    return mm * 2.83465

# Define your custom page sizes
A0 = (mm_to_points(841), mm_to_points(1189))
A1 = (mm_to_points(594), mm_to_points(841))
A2 = (mm_to_points(420), mm_to_points(594))
A3 = (mm_to_points(297), mm_to_points(420))

# Sizes to be used
sizes = {"A0": A0, "A1": A1, "A2": A2, "A3": A3}

# input_pdf_path = "./toughcad/74490 BLOCK B CEILING TIE LEVEL TRUSS LAYOUT - CONSTRUCTION.pdf"
input_pdf_path = "./toughcad/Firwood Ground Floor September 2023-Fire infomation.pdf"

# Read the PDF file
with open(input_pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    content = page.extract_text()

# Write the contents to new PDF files with the desired page sizes
for size_name, size in sizes.items():
    c = canvas.Canvas(f"output_{size_name}.pdf", pagesize=size)
    textobject = c.beginText()
    textobject.setTextOrigin(10, size[1] - 10)  # Set origin
    textobject.setFont("Helvetica", 14)  # Set font and size

    # Add the text from the original PDF file
    lines = content.split('\n')
    for line in lines:
        textobject.textLine(line)

    c.drawText(textobject)
    c.save()
