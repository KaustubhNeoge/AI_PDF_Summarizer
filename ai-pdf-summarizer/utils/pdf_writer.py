from reportlab.pdfgen import canvas
from io import BytesIO

def create_summary_pdf(summary_text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, "PDF Summary")

    c.setFont("Helvetica", 12)
    y = 760
    for line in summary_text.split("\n"):
        c.drawString(50, y, line[:100])
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()
    buffer.seek(0)
    return buffer
