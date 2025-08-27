from json import dumps, loads, dump, load


json_string = '{"name" : "Джон", "Возраст" : 36, "kids" : ["Mike", "Anna"], "pets": {"dog": "Rex", "cat": "Tom"}, "wife" : {"name" : "Jane", "age" : 35}}'  # json строка
print(json_string)

json_object = loads(json_string)  # создаем json объект из строки
print(json_object)

json_string = dumps(json_object, indent=4, ensure_ascii=False)  # создаем строку из json объекта
print(json_string)

json_object = {"name" : "Джон", "Возраст" : 36, "kids" : ("Mike", "Anna")}

with open("data.json", "w", encoding="utf8") as file:  # открываем файл
    dump(json_object, file, indent=4, ensure_ascii=False)  # записываем json объект в файл)


with open("data.json", "r", encoding="utf8") as file:  # открываем файл
    json_object = load(file)  # читаем json объект из файла
    print(json_object)