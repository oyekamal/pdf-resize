import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def resize_pdf(input_path, output_path, target_size):
    sizes = {
        "A0": (841, 1189),
        "A1": (594, 841),
        "A2": (420, 594),
        "A3": (297, 420),
    }

    if target_size not in sizes:
        print(f"Invalid target size: {target_size}")
        return

    target_width, target_height = sizes[target_size]

    # Read the input PDF
    reader = PdfReader(input_path)
    original_pages = reader.pages

    # Create a new PDF with the desired size
    with open(output_path, "wb") as output_file:
        writer = PdfWriter()

        for original_page in original_pages:
            # Create a canvas and scale the content to fit the new size
            packet = io.BytesIO()
            new_canvas = canvas.Canvas(packet, pagesize=(target_width, target_height))
            new_canvas.scale(target_width / letter[0], target_height / letter[1])

            # Draw the content of the original page onto the new canvas
            new_canvas.doForm(orig_page)
            new_canvas.save()

            # Move the buffer position to the beginning
            packet.seek(0)

            # Add the modified page to the new PDF
            new_pdf = PdfReader(packet)
            writer.add_page(new_pdf.pages[0])

        # Save the new PDF
        writer.write(output_file)

    print(f"PDF resized to {target_size}. Output saved to {output_path}")


# Example usage
input_pdf_path = "./toughcad/74490 BLOCK B CEILING TIE LEVEL TRUSS LAYOUT - CONSTRUCTION.pdf"
output_pdf_path = "output_resized.pdf"
target_size = "A3"

resize_pdf(input_pdf_path, output_pdf_path, target_size)
