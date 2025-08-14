import argparse
from pdfReader import readPdfGS
import strings
import processPath
import processText


def run_cli(argv):
    parser = argparse.ArgumentParser(description=strings.CLI_DESCRIPTION)
    parser.add_argument("path", help=strings.PDF_PATH_LABEL)
    args = parser.parse_args(argv)

    texts = processPath.processPath(args.path)
    facturas = processText.processText(texts)
    print(facturas)
