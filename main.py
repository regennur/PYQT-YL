#!/usr/bin/python3
# -*- coding: utf-8 -*-

from NoteDb import NoteDb
import sys
import sqlite3
from PyQt6.QtWidgets import (QListWidget, QWidget,
                             QApplication, QVBoxLayout)
import winsound


class NotesList(QWidget):

    def __init__(self):
        super().__init__()
        conn = sqlite3.connect('note_chastota.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        note_db = NoteDb(conn, cur)
        self.note_db = note_db

        self.initUI()

    def initUI(self):
        note_db = self.note_db
        all_nota_data = note_db.getAll()

        vbox = QVBoxLayout(self)

        listWidget = QListWidget()

        if not all_nota_data:
            return false

        for elem in all_nota_data:
            listWidget.addItem(elem["nota"])

        listWidget.itemClicked.connect(self.onClicked)

        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(30, 30, 100, 300)
        self.setWindowTitle('Note\'s player')
        self.show()

    def onClicked(self, item):
        note_db = self.note_db
        nota_chastota = note_db.get(item.text())

        # немного не чистые ноты, из-за того что на вход принимает integer
        winsound.Beep(round(nota_chastota), 980)


StyleSheet = '''
QWizardPage {
    background-color: rgb(100, 133, 202);
}
QListWidget {
    spacing: 5px;   
    background-color: rgb(17, 96, 98);
    color: rgb(255, 255, 255);
}
'''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)

    li = NotesList()

    sys.exit(app.exec())
