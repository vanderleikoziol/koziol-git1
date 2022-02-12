import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><strong>Programa&ccedil;&atilde;o em Python: Esencial</strong>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
