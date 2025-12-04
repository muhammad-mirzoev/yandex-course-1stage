from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches, Pt, Mm
import sys

data = list(map(lambda x: x.replace('\n', ''), sys.stdin.readlines()))

document = Document()

p1 = document.add_paragraph(data[0])
p1.style = document.styles.add_style('P', WD_STYLE_TYPE.PARAGRAPH)
font = p1.style.font
font.name = 'Arial'
font.size = Pt(11)
font.italic = True
p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT

style = document.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(12)

for i in data[1:-2]:
    p = document.add_paragraph(i)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_fmt = p.paragraph_format
    p_fmt.first_line_indent = Inches(0.5)

p2 = document.add_paragraph(data[-2])
p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
fmt = p2.paragraph_format
fmt.space_after = Mm(0)
p3 = document.add_paragraph(data[-1])
p3.alignment = WD_ALIGN_PARAGRAPH.LEFT
p3.style = document.styles.add_style('P3', WD_STYLE_TYPE.PARAGRAPH)
font = p3.style.font
font.bold = True

document.save('letter.docx')
