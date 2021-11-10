#!/usr/bin/python3
# -*- coding: utf-8 -*-

from NoteDb import NoteDb
import sys
import sqlite3
from PyQt6.QtWidgets import (QListWidget, QWidget, QMessageBox,
                             QApplication, QVBoxLayout)


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

        self.setGeometry(30, 30, 30, 300)
        self.setWindowTitle('QListWidget')
        self.show()

    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())
        print(item.text())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    li = NotesList()

    sys.exit(app.exec())
