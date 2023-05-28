from docx import Document
from docx.shared import Inches
document=Document()

document.add_picture(
    'Projects/cat.jpg',
    width=Inches(2.0)
    )

name=input('Enter your name:')
PhNo=input('Enter your Phone number"')
email=input('Enter your Email ID:')

document.add_paragraph(name+'|'+str(PhNo)+'|'+email)

document.save('cv.docx')