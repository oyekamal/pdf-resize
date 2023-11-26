from pdf2image import convert_from_path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
input_pdf_path = "./toughcad/74490 BLOCK B CEILING TIE LEVEL TRUSS LAYOUT - CONSTRUCTION.pdf"
def mm_to_points(mm):
    return mm * 2.83465

# Define your custom page sizes
A0 = (mm_to_points(841), mm_to_points(1189))
A1 = (mm_to_points(594), mm_to_points(841))
A2 = (mm_to_points(420), mm_to_points(594))
A3 = (mm_to_points(297), mm_to_points(420))

# Sizes to be used
sizes = {"A0": A0, "A1": A1, "A2": A2, "A3": A3}

# Convert PDF to images
pages = convert_from_path(input_pdf_path)

# Resize images and save them
resized_pages = []
for i, page in enumerate(pages):
    # Resize page
    resized_page = page.resize(sizes["A0"])  # Change to the size you want
    # Save resized page to a file
    resized_page.save(f"resized_page_{i}.png", "PNG")
    # Add to list
    resized_pages.append(f"resized_page_{i}.png")

# Create a new PDF
c = canvas.Canvas("resized.pdf", pagesize=sizes["A0"])  # Change to the size you want

# Add images to PDF
for page in resized_pages:
    c.drawImage(page, 0, 0, width=sizes["A0"][0], height=sizes["A0"][1])  # Change to the size you want
    c.showPage()

# Save PDF
c.save()
