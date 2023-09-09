from fpdf import FPDF
from PIL import Image

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()


pdf.set_x(0)
pdf.set_y(10)
pdf.set_font("helvetica", "B", 40)
pdf.cell(200,50,'CS50 Shirtificate', align='C')

pdf.image("shirtificate.png", x=10,y=60,w=pdf.w*.9)

pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", "B", size=30)
pdf.set_y(100)
pdf.set_x(0)
pdf.cell(210,50, f'{name} took CS50', align = 'C')


pdf.output("shirtificate.pdf")


'''
img = Image.open("shirtificate.png")
print(img.size)
'''
