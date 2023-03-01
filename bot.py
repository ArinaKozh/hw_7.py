from random import *
import json

lst=[]


def save():
    with open("data.json","w",encoding="utf-8") as f:
        f.write(json.dumps(lst,ensure_ascii=False))
    print("Данные успешно сохранены")

def load():
    global lst
    with open("data.json","r",encoding="utf-8") as f:
        lst=json.load(f)
    print("Данные успешно загружены")  

def clear():
    with open("data.json", "w") as f:
        pass 

try:
    load()
except:
    lst.append("Встать")
    lst.append("Почистить зубы")
    lst.append("Сделать домашку GB")
  

while True:
    command = input("Введите команду\n")
    if command=="/start":
        print("Бот-список дел начал работу")
    elif command=="/stop":
        save()
        print("До свидания, заходите еще!")
        break
    elif command=="/all":
        print("Вот текущий список дел:")
        print(lst)
    elif command =="/add":
        task=input("Введите дело, которое хотите добавить\n")
        lst.append(task)
        print(f'"{task}" успешно добавлено в список дел')
    elif command=="/help":
        print("Вы можете написать боту следущие команды: \n"
              "start - начать работу\n"
              "stop - закончить работу\n"
              "all - показать список всех дел\n"
              "add - добавить дело\n"
              "delete - удалить дело из списка дел\n"
              "clear - очистить список дел\n"
                 
                 )
    elif command=="/delete":
        task=input("Введите задание, которое хотите удалить\n")
        try:
            lst.remove(task)
            print(f'"{task}"Успешно далено из списка дел')
        except:
            print(f'Дело "{task}" не найдено в списке')
    elif command=="/clear":
        clear()
        lst = []
    elif command =="/save":
        save()
    elif command=="/load":
        load()
    else:
        print('Неопознанная команда. Чтобы увидеть список доступных команд, введите "/help"')