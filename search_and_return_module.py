import sqlite3
conn = sqlite3.connect('notes.db', check_same_thread=False)
cur = conn.cursor()


# "AND" - поиск когда все параметры есть в записи
def search_full(text):
    print('Идет поиск, подождите...')
    all_columns = ["noteid", "title", "note", "author", "last_modified"]
    resault = []
    res_list = []
    end_list = []
    for i in text:
        for j in all_columns:
            cur.execute(f"select * from notes where {j}='{i}'")
            resault = cur.fetchall()
            if resault:
                res_list += resault
    for i in res_list:
        if res_list.count(i) == len(text):
            if i not in end_list:
                end_list.append(i)
                print(end_list)

    return end_list


# "OR" поиск когда любой параметр есть в записи
def search_or(text):
    print('Идет поиск(OR)), подождите...')
    all_columns = ["noteid", "title", "note", "author", "last_modified"]
    resault = []
    res_list = []
    for i in text:
        for j in all_columns:
            cur.execute(f"select * from notes where {j}='{i}'")
            resault = cur.fetchall()
            if resault!= []:
                if resault[0] not in res_list:   # блок для отсеивания повторных записей если 2 и более элементы встерчаются в одной записи
                    res_list += resault
    print(res_list)
    return res_list





# Вывод всех данных из таблицы
def search_all():
    cur.execute("SELECT * FROM notes")
    result_list = cur.fetchall()
    return_list = [list(i) for i in result_list]
    return return_list
