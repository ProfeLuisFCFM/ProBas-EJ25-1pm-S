from random import randint

from funciones import Triangulo,Circulo

c1 = Circulo(360)
print(c1.sumarNumeros(1,2,3,4,5,6,7,8,9,10,11))
t1 = Triangulo()


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(h=10, w=0, txt="hello world \n", border=1)
pdf.cell(h=10, w=0, txt=str(c1.sumarNumeros(1,2,3,4,5,6,7,8,9,10,11))+"\n", border=1)
pdf.cell(h=10, w=0, txt="bye disgusting", border=1)
pdf.output("hello_world.pdf")


import pandas as pd

df = pd.read_csv("test.csv", encoding="utf8")

print(df)