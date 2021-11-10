class NoteDb:
    # тестовые данные
    _notes_data = [
        ('до', 261.63),
        ('до#', 277.18),
        ('ре', 293.66),
        ('ре#', 311.13),
        ('ми', 329.63),
        ('фа', 349.23),
        ('фа#', 369.99),
        ('соль', 392.00),
        ('соль#', 415.30),
        ('ля', 440.00),
        ('ля#', 466.16),
        ('си', 493.88),
        ('до2', 523.25)
    ]

    def __init__(self, conn, cur):
        super().__init__()

        self.conn = conn
        self.cur = cur

    def create(self):
        '''создает базу данных music, 
        если она не существует'''
        cur = self.cur
        conn = self.conn

        cur.execute(
            'CREATE TABLE IF NOT EXISTS music (nota PRIMARY KEY, chastota)')
        conn.commit()

    def fill(self):
        '''заполняет базу данными'''
        notes_data = self._notes_data
        cur = self.cur
        conn = self.conn

        for elem in notes_data:
            cur.execute('INSERT INTO music VALUES(?,?)', elem)
            conn.commit()

    def get(self, note_title):
        '''получает частоту по названию ноты'''
        cur = self.cur
        conn = self.conn

        result = cur.execute("""SELECT * FROM music
            WHERE nota = ?""", (note_title,)).fetchone()

        if not result:
            print(note_title, "не существует в базе данных")
            return False

        return result["chastota"]

    def getAll(self):
        '''получает все частоты'''
        cur = self.cur

        result = cur.execute("""SELECT * FROM music""").fetchall()

        if not result:
            print("база данных пуста")
            return False

        return result
