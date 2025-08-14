
import subprocess
import os


def readPdfGS(pdf_path: str) -> bool:

    if os.name == 'nt':
        ghostscriptBin = "gswin64c"
    else:
        ghostscriptBin = "gs"

    result = subprocess.run(
        [
            ghostscriptBin,
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

    if result.returncode != 0:
        print("Error en Ghostscript:", result.stderr)
        return None

    return result.stdout
