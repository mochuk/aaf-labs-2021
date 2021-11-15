import re

arr_tree = []
names = []

def find_words(line):
    #ділимо за пробілами рядок на слова
    arr_words = re.findall(r'\w+', line)
    #шукаємо команду
    if re.match(r'^[Cc][Rr][Ee][Aa][Tt][Ee]\b', arr_words[0]):
        create(arr_words)
    elif re.match(r'^[Ii][Nn][Ss][Ee][Rr][Tt]\b', arr_words[0]):
        insert(arr_words, line)
    elif re.match(r'^[Pp][Rr][Ii][Nn][Tt][_][Tt][Rr][Ee][Ee]\b', arr_words[0]):
        print_tree(arr_words)
    elif re.match(r'^[Cc][Oo][Nn][Tt][Aa][Ii][Nn][Ss]\b', arr_words[0]):
        contains(arr_words, line)
    elif re.match(r'^[Ss][Ee][Aa][Rr][Cc][Hh]\b', arr_words[0]):
        search(arr_words, line)
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

def insert(arr_words, line):
    k=0
    m=0
    #дістаємо ім'я множини
    name = arr_words[1]
    #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
    if (name in names):
        #перевіряємо правильність команди
        if re.search(r'[,]', line):
            #дістаємо значення x та у
            a = re.split(r'[(]', line)
            b = re.split(r'[)]', a[1])
            c = re.findall(r'\w', b[0])
            for i in range(len(c)):
                if (c[i] == ','):
                    k = i-1
                    return k
            for j in range(1, k):
                temp1 = []
                temp1.append(c[j])
                return temp1
            for l in range(k,len(c)):
                temp2 = []
                temp2.append(c[l])
                return temp2
            x = temp1.join('')
            y = temp2.join('')
            #записуємо х та у
            for i in range(len(arr_tree)):
                if (arr_tree[i][0] == name):
                    m = i
                    return m
            arr_tree[m].append([x, y])
            print(arr_tree)
            print("Точка (", x, ",", y, ") була додана до ", name, "\n")
        else:
            print("Неправильно введена команда 'INSERT'")
    else:
        print("Точка не була додана до ", name, ", бо множина з таким іменем не існує\n")

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

def contains(arr_words, line):
    #дістаємо ім'я множини
    name = arr_words[1]
    #перевіряємо наявність цієї множини (співпадіння назви з одним із елементів масиву)
    if (name in names):
        #перевіряємо правильність команди
        if re.search(r'[,]', line):
            #дістаємо значення x та у
            a = re.split(r'[(]', line)
            b = re.split(r'[)]', a[1])
            c = re.findall(r'\w', b[0])
            for i in range(len(c)):
                if (c[i] == ','):
                    k = i-1
                    return k
            for j in range(1, k):
                temp1 = []
                temp1.append(c[j])
                return temp1
            for l in range(k,len(c)):
                temp2 = []
                temp2.append(c[l])
                return temp2
            x = temp1.join('')
            y = temp2.join('')
            #шукаємо х та у
            for i in range(len(arr_tree)):
                if (arr_tree[i][0] == name):
                    m = i
                    return m
            for j in range(len(arr_tree[m])):
                if (arr_tree[m][j][0] == x):
                    if (arr_tree[m][j][1] == x):
                        print('True')
                else:
                    print('False')
        else:
            print("Неправильно введена команда 'CONTAINS'")
    else:
        print("Точка не була додана до ", name, ", бо множина з таким іменем не існує\n")

def search(arr_words, line):
    k = 0
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
    #перевіряємо правильність команди WHERE
    elif re.match(r'^[Ww][Hh][Ee][Rr][Ee]\b', arr_words[2]):
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
                print("Неправильно введена команда 'ABOVE_TO'")
        #перевіряємо правильність команди NN
        elif re.match(r'^[Nn][Nn]\b', arr_words[3]):
            #перевіряємо правильність команди
            if re.search(r'[,]', line):
                #дістаємо значення x та у
                a = re.split(r'[(]', line)
                b = re.split(r'[)]', a[1])
                c = re.findall(r'\w', b[0])
                for i in range(len(c)):
                    if (c[i] == ','):
                        k = i-1
                        return k
                for j in range(1, k):
                    temp1 = []
                    temp1.append(c[j])
                return temp1
                for l in range(k,len(c)):
                    temp2 = []
                    temp2.append(c[l])
                    return temp2
                    x = temp1.join('')
                    y = temp2.join('')
                print("Найближчий сусід точки (", x, ",", y, ") точка ...")
            else:
                print("Неправильно введена команда 'NN'")
        #перевіряємо правильність команди INSIDE
        elif re.match(r'^[Ii][Nn][Ss][Ii][Dd][Ee]\b', arr_words[3]):
            #перевіряємо правильність команди
            #if re.search(r'[,]', line):
                #дістаємо значення x та у
                #a = re.split(r'[(]', line)
                #b = re.split(r'[)]', a[1])
                #c = re.findall(r'\w', b[0])
                #for i in range(len(c)):
                    #if (c[i] == ','):
                        #k = i-1
                        #return k
                #for j in range(1, k):
                    #temp1 = []
                    #temp1.append(c[j])
                #return temp1
                #for l in range(k,len(c)):
                    #temp2 = []
                    #temp2.append(c[l])
                    #return temp2
                    #x = temp1.join('')
                    #y = temp2.join('')
                #print("Найближчий сусід точки (", x, ",", y, ") точка ...")
                print("прямокутник...")
            #else:
                #print("Неправильно введена команда 'INSIDE'")
    else:
        print ("Неправильно введена команда 'SEARCH'")

while True:
    line = input()
    find_words(line)
