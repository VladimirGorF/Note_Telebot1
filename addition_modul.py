import sqlite3
import datetime

conn = sqlite3.connect('notes.db', check_same_thread=False)
cur = conn.cursor()

id_count = 0


def find_max_id():
    global id_count
    cur.execute("SELECT noteid FROM notes;")
    all_results = cur.fetchall()
    for i in all_results:
        if id_count < i[0]:
            id_count = i[0]
    id_count += 1


def add_note(data_list):
    global id_count
    data_list = " ".join(data_list)
    data_list = data_list.split(";")
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")
    find_max_id()
    data_list.insert(0, id_count)
    data_list.append(time)
    print(data_list)
    cur.execute("""INSERT INTO notes VALUES(?, ?, ?, ?, ? );""", data_list)
    conn.commit()
    id_count -= 1

