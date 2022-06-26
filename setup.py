import datetime
import os
import sqlite3
import webbrowser
import sys
from bd.conectar import connectarbd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (Frame, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle, Image)

from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","sys"], "includes": ["PyQt5","sqlite3", "reportlab"],}

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
