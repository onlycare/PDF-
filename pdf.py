import glob
import fitz
import os


def pictopdf():
    doc = fitz.open()
    for img in glob.glob(r"pdf/*"):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    if os.path.exists("newpdf.pdf"):        # 若文件存在先删除
        os.remove("newpdf.pdf")
    doc.save("newpdf.pdf")                   # 保存pdf文件
    doc.close()

if __name__ == '__main__':
    pictopdf()


