import os
import img2pdf

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\images"



print(__location__)

with open("ImageContainBook.pdf","wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir((__location__ )) if i.endswith(".jpg")]))
    
