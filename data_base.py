import sqlite3
conn = sqlite3.connect('notes.db')
cur = conn.cursor()

# Создание БД
# cur.execute("""CREATE TABLE notes(
#    noteid INT PRIMARY KEY,
#    title TEXT,
#    note TEXT,
#    author TEXT,
#    last_modified TEXT);
# """)
# conn.commit()
#
# notes = [
#   ('0', 'Groza', 'Description of popular book in Russia','Vladimir Gorbunov','09.03.2023'),
#   ('1', 'Tor', 'Description of popular film in America','Vladimir Gorbunov','09.03.2023'),
#   ('2', 'Flower', 'So much flowers grow  in Russia today','Vladimir Gorbunov','09.03.2023'),
#   ('3', 'Rubble', 'Rubble is going to be upper-value in future','Vladimir Gorbunov','09.03.2023')
#
# ]
# cur.executemany("INSERT INTO notes VALUES(?, ?, ?, ?, ?);", notes)
# conn.commit()



