#!/usr/bin/env python3

"""— Написати скрипт, який отримує в якості аргументів пари значень
name:salary (наприклад ./rank.py john:1000.5 bob:850 klaus:1100).
-Скрипт виводить значення відсортовані за зростанням
(якщо передано аргумент --inv або спаданням — за замовчуванням).
-А також форматує імена, щоб вони починались з великої літери (метод title).
-Якщо ім'я повторюється, скрипт має писати зарплати у вигляді діапазону (від мінімальної до максимальної).
-Вивід у форматі таблиці (ширина поля імені задається найдовшим іменем з переліку) 
"""

USAGE = """USAGE: {script} You should write: name(str):salary(int/float)
"""
USAGE = USAGE.strip()


def creat_slovar(list):
    if "--inv" in list :        #перевірка на "--inv"
        list.remove("--inv")
        flag = True             # якщо "--inv" присутній сортування по зарплаті
    else: flag =False           # якщо "--inv" відсутній сортування по алфавіту імені прізвища
                   
    #створення словника    
    slovar = {}
    for i in list:
        k, v = i.split(":")
        slovar[k]= slovar.get(k, []) +[int(v)]

    #coртування  в залежності від "флагу"
    if flag:
        spisok = {k: slovar[k] for k in sorted(slovar, key=lambda x: slovar[x])}  # якщо "--inv" присутній сортування по зарплаті      
    else :
        spisok = {k: slovar[k] for k in sorted(slovar, key=lambda x: x)}   # якщо "--inv" відсутній сортування по алфавіту імені прізвища
        
    #-А також форматує імена, щоб вони починались з великої літери (метод title).
    #-Якщо ім'я повторюється, скрипт має писати зарплати у вигляді діапазону (від мінімальної до максимальної) 
    new_spisok = {}
    for k, v in spisok.items():
        new_spisok[k.title()] = sorted(v)
    data = [["Name", "Salary $$$"], new_spisok]
    return data
##############################################################################################################################
def create_table(data, header_separator=True):
    doc = creat_slovar(data)
    header_cols = len(doc[0])

    #Зрбив щоб "Name" i "Salery" виводилися в якості заголовка
    elem_col1 = [doc[0][0]] + list(doc[1].keys())
    elem_col2 = [doc[0][1]] + (list(map(str, list(doc[1].values()))))


    # Визначає ширину кожного стовпчика
    col_width = [len(max(elem_col1, key=len)),
                 len(max(elem_col2, key=len))]

    # Межі заголовків кожного стовпчика
    separator = "-+-".join('-' * n for n in col_width)

    # Створення таблиці
    i = 0
    for col in range(len(elem_col1)):
        if i == 1:
            print(separator)
        result = [elem_col1[col].rjust(col_width[0]),
                  elem_col2[col].rjust(col_width[1])]
        i += 1
        print(" | ".join(result))
#################################################################################################################################
def main(args):
    """Gets called when run as a script."""
    if len(args) < 2 :
        exit(USAGE.format(script=args[0]))

    create_table((sys.argv[1:]))
    



if __name__ == '__main__':
    import sys

    main(sys.argv)
