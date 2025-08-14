#!/usr/bin/python3
import sys
from gui.main import Aplicacion
from cli.main import run_cli

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli(sys.argv[1:])
    else:
        app = Aplicacion()
        app.run()
