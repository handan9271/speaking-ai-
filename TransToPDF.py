from docx2pdf import convert
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import datetime

def TransToPDF(name):
    # today = GWord.today
    # name = GWord.name
    today = datetime.date.today()
    # 定义路径
    input_docx = f'./results/{name}_Speaking_{today}.docx'
    output_pdf = f'./results/{name}_Speaking_{today}.pdf'
    watermarked_pdf = f'./results/{name}_Speaking_{today}.pdf'

    # 创建转换任务
    convert(input_docx, output_pdf)

    # 创建水印
    packet = io.BytesIO()
    # Create a canvas to draw the watermark
    can = canvas.Canvas(packet, pagesize=letter)
    # Set up the watermark properties
    watermark_text = f"""IELTS examiner Nick AI team"""
    font_size = 40
    opacity = 0.1  # 30% opacity
    can.setFont("Helvetica", font_size)
    can.setFillColorRGB(0, 0, 0, alpha=opacity)
    text_width = can.stringWidth(watermark_text, "Helvetica", font_size)
    # Calculate the position (centered)
    # For a standard letter page size (8.5 x 11 inches), assuming the page is rotated
    page_width, page_height = letter[1], letter[0]  # Swap dimensions for rotated page
    x = (page_width - text_width) / 2
    y = (page_height - font_size) / 2
    can.translate(x, y)
    can.rotate(45)
    can.drawString(0, 0, watermark_text)
    can.save()


    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfReader(packet)
    # Read the existing PDF
    existing_pdf = PdfReader(open(output_pdf, "rb"))
    output = PdfWriter()

    # Add watermark to each page
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


    # Write the watermarked PDF
    with open(watermarked_pdf, "wb") as f:
        output.write(f)

    # watermarked_pdf

