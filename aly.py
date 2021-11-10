# import sqlite3


# base = sqlite3.connect('note_chastota.db')
# cur = base.cursor()


# base.execute('CREATE TABLE music(nota PRIMARY KEY, chastota)')
# base.commit()

# tablitza = [
#     ('до', 261.63),
#     ('до#', 277.18),
#     ('ре', 293.66),
#     ('ре#', 311.13),
#     ('ми', 329.63),
#     ('фа', 349.23),
#     ('фа#', 369.99),
#     ('соль', 392.00),
#     ('соль#', 415.30),
#     ('ля', 440.00),
#     ('ля#', 466.16),
#     ('си', 493.88),
#     ('до2', 523.25)
# ]

# for elem in tablitza:
#     cur.execute('INSERT INTO music VALUES(?,?)', elem)
#     base.commit()


# notaWwod = input()

# result = cur.execute("""SELECT * FROM music
#             WHERE nota = ?""", (notaWwod,)).fetchall()

# chastt = str(result)
# if len(chastt) == 16:
#     chassDann = chastt[7:14:]
#     freq = float(chassDann)
# else:
#     chassDann = chastt[8:15:]
#     freq = float(chassDann)


# print(freq)

import sqlite3
from NoteDb import NoteDb

conn = sqlite3.connect('note_chastota.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

note_db = NoteDb(conn, cur)
note_db.get("до")
