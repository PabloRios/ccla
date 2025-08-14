
def processPath(path):
    import os
    import glob
    from pdfReader import readPdfGS

    pdfs = glob.glob(os.path.join(path, "*.pdf"))
    facturasText = []
    for pdf in pdfs:
        facturasText.append(readPdfGS(pdf))

    return facturasText
