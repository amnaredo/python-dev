import PyPDF2


def pdf_watermark(pdf_wtr, pdf_file):

    output = PyPDF2.PdfFileWriter()
    reader_file = PyPDF2.PdfFileReader(pdf_file)
    reader_wtr = PyPDF2.PdfFileReader(pdf_wtr)
    wtr_page = reader_wtr.getPage(0)
    for i in range(reader_file.getNumPages()):
        page = reader_file.getPage(i)
        page.mergePage(wtr_page)
        output.addPage(page)

    with open('newfile.pdf', 'wb') as f:
        output.write(f)


pdf_watermark('wtr.pdf', 'dummy.pdf')
