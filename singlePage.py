import PyPDF4

def resize_pdf(input_path, output_path, size):
    with open(input_path, 'rb') as file:
        pdf = PyPDF4.PdfFileReader(file)
        writer = PyPDF4.PdfFileWriter()

        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            page.scaleTo(size[0], size[1])
            writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)


size = (841, 1189)  # A2 size

# Example usage
input_file = input_pdf_path = "./toughcad/A95E6320A  12x10 PA (2).PDF"

output_file = 'output_pages.pdf'

resize_pdf(input_file, output_file, size)
