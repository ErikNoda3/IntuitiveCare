import tabula #pip install tabula-py[jpype]
import pandas as pd

#abrir o pdf
pdf_path = "Anexo1.pdf"
tabelas = tabula.read_pdf(pdf_path, pages="3")
tabela = tabelas[0]
print(tabela)