import sqlite3
import datetime


conn = sqlite3.connect('notes.db', check_same_thread=False)
cur = conn.cursor()

def sql_update(list_param):    # принимает  входящий спискок изменений
    all_columns = ["noteid", "title", "note", "author", "last_modified"]
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")
    print('change_module is working')
    print(list_param)

    list_param = " ".join(list_param)
    list_param = list_param.split(";")
    print(list_param)

    for i in range(1, len(list_param)):
        if not list_param[i]:
            print('Not value')
        else:                      # изменяет данные в соответствуещем поле
            cur.execute(f' UPDATE notes SET {all_columns[i]} = "{list_param[i]}" where noteid = {list_param[0]}')
            conn.commit()

    cur.execute(f' UPDATE notes SET {all_columns[4]} = "{time}" where noteid = {list_param[0]}')  #вносит дату и время
    conn.commit()

