import re

arr_tree = [["tree"]]
names = []

def find_words(line):
    #ділимо за пробілами рядок на слова
    arr_words = re.findall(r'\w+', line)
    #виводимо масив слів
    print(arr_words)
    #шукаємо команду
    if re.match(r'^[Cc][Rr][Ee][Aa][Tt][Ee]', arr_words[0]):
        create(arr_words)
    elif re.match(r'^[Ii][Nn][Ss][Ee][Rr][Tt]', arr_words[0]):
        insert(arr_words)
    elif re.match(r'^[Pp][R][Ii][Nn][Tt][_][Tt][Rr][Ee][Ee]', arr_words[0]) :
        print_tree(arr_words)
    elif re.match(r'^[Cc][Oo][Nn][Tt][Aa][Ii][Nn][Ss]', arr_words[0]):
        contains(arr_words)
    elif re.match(r'^[Ss][Ee][Aa][Rr][Cc][Hh]', arr_words[0]):
        search(arr_words)
    else:
        print("Неправильна назва команди або назва команди відсутня взагалі")

def create(arr_words):
    #дістаємо ім'я множини
    name=arr_words[1]
    #перевіряємо правильність команди
    if (len(arr_words) == 2):
        #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
        if (name in names):
            print("Множина", name, "не була створена, бо вже існує множина з таким іменем\n")
            print(names)
        else:
            names.append(name)
            arr_tree.append([name,[]])
            print("Множина", name, "була створена\n")
            print(arr_tree)
    else:
        print("Неправильно введена команда 'CREATE'")

def insert(arr_words):
    #дістаємо ім'я множини
    name = arr_words[1]
    #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
    if (name in names):
        #перевіряємо правильність команди
        if (len(arr_words) <= 7):
            if (len(arr_words) >= 3):
                #(x,y)
                if (len(arr_words) == 3):
                    #дістаємо значення x та у
                    r10 = re.split(r'[(]', arr_words[2]) #['x,y)']
                    r11 = re.split(r'[)]', r10[0]) #['x,y']
                    r = re.split(r'[,]', r11[0]) #['x', 'y']
                    x = r[0]
                    y = r[1]
                #(x, y) (x ,y)
                elif (len(arr_words) == 4):
                    #дістаємо значення x та у
                    r10 = re.split(r'[(]', arr_words[2]) #['x,'] ['x']
                    r11 = re.split(r'[,]', r10[0]) #['x']
                    r20 = re.split(r'[)]', arr_words[3]) #['y'] [',y']
                    r21 = re.split(r'[,]', r20[0]) #['y']
                    x=r11[0]
                    y=r21[0]
                #(x , y) (x ,y ) ( x, y)
                elif (len(arr_words) == 5):
                    #дістаємо значення x та у
                    r10 = re.split(r'[(]', arr_words[2]) #['x'] ['x'] ['']
                    r20 = re.split(r'[)]', arr_words[4]) #['y'] [''] ['y']
                    if (r10[0] != NULL):
                        x=r10[0]
                    else:
                        r30 = re.split(r'[,]', arr_words[3]) #['x']
                        x=r30[0]
                    if (r20[0] != NULL):
                        y=r20[0]
                    else:
                        r30 = re.split(r'[,]', arr_words[3]) #['y']
                        y=r30[0]
                #(x , y ) ( x , y)
                elif (len(arr_words) == 6):
                    if ((arr_words[3] == ',') or (arr_words[4] == ','))
                        #дістаємо значення x та у
                        r10 = re.split(r'[(]', arr_words[2]) #['x'] ['']
                        r20 = re.split(r'[)]', arr_words[5]) #[''] ['y']
                        if (r10[0] != NULL):
                            x=r10[0]
                        else:
                            r30 = re.split(r'[,]', arr_words[3]) #['x']
                    else:


                #( x , y )
                else:
                #дістаємо значення x та у



            """
                """"""То что что в скобках
                проверка на скобки
                создать массив temp и в него запихнуть temp[0] and temp[1]
                If(первый элемент был пустой)
                    записываем первый элемент
                else(первый элемент не пустой)
                    i -- зависит от имени (порядок в массиве)
                    arr_tree[i].append(...)
                """"""
                #додаємо назву множини і точку в масив
                arr_tree.append([])
                arr_tree[-1].append(set_name)
                arr_tree[-1].append(c)
                print("Точка (", a, ",", b, ") була додана до ", set_name, "\n")
            else:
                print("Точка ", (x, y), " була додана до ", set_name, ", бо множина з таким іменем не існує\n")
            """

            else:
                print("Неправильно введена команда 'INSERT'")
        else:
            print("Неправильно введена команда 'INSERT'")
        #додаємо точку до множини з ім'ям name


    else:
        print("Точка не була додана до", name, ", бо множина з таким іменем не існує\n")

def print_tree(arr_words):
    #дістаємо ім'я множини
    name = arr_words[1]
    #перевіряємо правильність команди
    if (len(arr_words) == 2):
        #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
        if (name not in names):
            print("Внутрішня структура KD-дерева, побудованого для множини", name, "не була виведена, бо множина з таким іменем не існує\n")
            print(names)
        else:
            print("Внутрішня структура KD-дерева, побудованого для множини", name, "\n")
            for i in range(len(arr_tree)):
                if (arr_tree[i][0] == name):
                    print(arr_tree[i])
            #тут буде функція виведення структури дерева
    else:
        print("Неправильно введена команда 'PRINT TREE'")

#""" def contains(arr_words):"""
#
def search(arr_words):
    k=
    #дістаємо ім'я множини
    name = arr_words[1]
    #перевіряємо правильність команди
    if (len(arr_words) == 2):
        #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
        if (name not in names):
            print("Всі точки із множини", name, "не були виведені, бо множина з таким іменем не існує\n")
            print(names)
        else:
            print("Всі точки із множини", name, "будуть виведені\n")
            for i in range(len(arr_tree)):
                if (arr_tree[i][0] == name):
                    k = i
                    return k
            for j in arr_tree[k][1:]:
                temp = []
                temp[0] = arr_tree[k][j][0]
                temp[1] = arr_tree[k][j][1]
                print('(' + temp[0]+ ',', temp[1] + ')')
    elif re.match(r'^[Ww][Hh][Ee][Rr][Ee]', arr_words[2]):
        if (len(arr_words) == 5):
            #дістаємо значення y
            y = arr_words[4]
            #перевіряємо правильність команди ABOVE_TO
            if re.match(r'^[Aa][Bb][Oo][Vv][Ee][_][Tt][Oo]', arr_words[3]):
                #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
                if (name not in names):
                    print("Пошук точок у множині", name, "не був проведений, бо множина з таким іменем не існує\n")
                    print(names)
                else:
                    print("Всі точки із множини", name, "координата y, яких більша за", у, "будуть виведені\n")
                    for i in range(len(arr_tree)):
                        if (array[i][0] == name):
                            k = i
                            return k
                    for j in range(len(arr_tree[k])):
                        if (arr_tree[k][j][1] > y):
                            print(arr_tree[k][j])
            else:
                print("Неправильно введена команда 'NN'")
        else:
            print("Неправильно введена команда 'WHERE'")
    """elif

            #тут буде функція виведення структури дерева
            print("Внутрішня структура KD-дерева, побудованого для множини", name, "\n")
            print(names)
    elif"""


    #else:
        #print ("Неправильно введена команда 'SEARCH'")


while True:
    line = input()
    find_words(line)
