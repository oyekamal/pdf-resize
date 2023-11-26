from pdf2image import convert_from_path
from PIL import Image, ImageFilter
from reportlab.pdfgen import canvas

def convert_pdf_to_image(pdf_path, output_folder, dpi=300):
    images = convert_from_path(pdf_path, output_folder=output_folder, dpi=dpi)
    return images

def resize_image(image, size, resample=Image.LANCZOS):
    resized_image = image.resize(size, resample=resample)
    return resized_image

def convert_images_to_pdf(images, output_pdf):
    pdf = canvas.Canvas(output_pdf)
    for img in images:
        pdf.setPageSize((img.width, img.height))
        pdf.drawInlineImage(img, 0, 0)
        pdf.showPage()
    pdf.save()

if __name__ == "__main__":
    pdf_path = input_pdf_path = "./toughcad/74490 BLOCK B CEILING TIE LEVEL TRUSS LAYOUT - CONSTRUCTION.pdf"

    output_folder = "temp_images"
    output_pdf = "resized_output.pdf"
    
    # Define the desired size (e.g., A4)
    desired_size = (595, 842)  # A4 size
    
    # Convert PDF to images with higher DPI for better quality
    images = convert_pdf_to_image(pdf_path, output_folder, dpi=400)
    
    # Resize each image with a better resampling method
    resized_images = [resize_image(img, desired_size, resample=Image.LANCZOS) for img in images]
    
    # Convert resized images back to PDF
    convert_images_to_pdf(resized_images, output_pdf)
