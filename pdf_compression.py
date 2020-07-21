import glob
import fitz
import os


pdffile = "xxxx.pdf"
doc = fitz.open(pdffile)
width, height = fitz.PaperSize("a4")

totaling = doc.pageCount

for pg in range(totaling):
    page = doc[pg]
    zoom = int(50)  # 设置百分比
    rotate = int(0)
    print(page)
    trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)

    lurl = 'pdf/%s.jpg' % str(pg + 1)
    pm.writePNG(lurl)
doc.close()



