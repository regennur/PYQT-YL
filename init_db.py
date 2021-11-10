import sqlite3
from NoteDb import NoteDb

conn = sqlite3.connect('note_chastota.db')
cur = conn.cursor()

note_db = NoteDb(conn, cur)
note_db.create()
note_db.fill()
