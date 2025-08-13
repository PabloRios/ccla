
import subprocess


def readPdfGS(pdf_path: str) -> bool:

    result = subprocess.run(
        [
            "gs",  # o "gswin64c" en Windows
            "-dBATCH",
            "-dNOPAUSE",
            "-dQUIET",
            "-sDEVICE=txtwrite",
            "-dFirstPage=1",
            "-dLastPage=1",
            "-sOutputFile=-",
            pdf_path
        ],
        capture_output=True,
        text=True
    )
    return result.stdout
