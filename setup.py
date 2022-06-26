import datetime
import os
import sqlite3
import webbrowser


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, letter
from reportlab.pdfgen import canvas
from reportlab.platypus import ( SimpleDocTemplate,Table, TableStyle, )
from view import Imagens
import sys

from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","sys","sqlite3", "reportlab","reportlab.lib","reportlab.pdfgen","reportlab.platypus","reportlab.lib.pagesizes"], "includes": ["PyQt5","reportlab","reportlab.lib","reportlab.pdfgen","reportlab.platypus","reportlab.lib.pagesizes"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Reserva_Treinamento",
    version="0.1",
    description="Controle de Reservas para sala de treinamento",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
