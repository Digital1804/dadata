from dadata import Dadata
from sqlib import *

token = input("Введите API-ключ: ")
secret = input("Введите секретный ключ: ")
lang = input("Выберите язык ответа (англ, рус): ")
if lang == "англ":
    lang = "en"
else:
    lang = "ru"
settings(token, secret, lang)


def find_street():
    data = Dadata(token, secret)
    while 1:
        street = input("Введите предполагаемый адрес или введите 0 для завершения программы: ")
        if street == "0":
            break
        datas = []
        res = data.suggest(name="address", query=street, language=lang)
        counter = 0
        for i in res:
            counter += 1
            print(f"#{counter} {i['value']}")
            datas.append(i['value'])
        ans = input("Введите номер подходящего адреса или введите 0 для возвращения к предыдущему шагу: ")
        ans = int(ans) - 1
        if ans == 0:
            continue
        res = data.suggest(name="address", query=datas[ans], language=lang, count=1)
        print("Ваш адрес ", res[0]['value'])
        print(f"Широта {res[0]['data']['geo_lat']}, Долгота {res[0]['data']['geo_lon']}")
    if input("Хотите удалить таблицу с настройками пользователей?(да/нет)") in ['да', 'нет']:
        drop()
    data.close()


if __name__ == '__main__':
    try:
        find_street()
    except Exception as e:
        print(f"Error {e}")

