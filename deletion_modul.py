import sqlite3
conn = sqlite3.connect('notes.db', check_same_thread=False)
cur = conn.cursor()

def del_note(note_id):
    cur.execute(f"""DELETE FROM notes WHERE noteid={note_id}""")
    conn.commit()
