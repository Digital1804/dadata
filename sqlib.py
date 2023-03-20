import sqlite3


def settings(token, secret, lang):
    url = "https://dadata.ru/api/suggest/address/"
    conn = sqlite3.connect("settings.db")
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS datas
    (url text, token text, api text, language text)''')
    data = (url, token, secret, lang)
    curs.execute("INSERT INTO datas VALUES (?, ?, ?, ?)", data)
    conn.commit()
    return 0


def drop():
    conn = sqlite3.connect("settings.db")
    curs = conn.cursor()
    curs.execute('''DROP TABLE IF EXISTS datas''')
    conn.commit()
    return 0

