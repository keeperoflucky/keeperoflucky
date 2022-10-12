box = [["*"]*3 for _ in range(3)] #сам массив

def show_box(f):
    print('  0 1 2')
    for i in range(len(box)):
       print(str(i), *box[i])

def player_input(f):
    while True:
        point = input('Введите две координаты от 0 до 2: ').split()
        if len(point) != 2:
            print('Введите две координаты через пробел: ')
            continue
        if not(point[0].isdigit() and point[1].isdigit()):
            print('Введите числа')
            continue
        x,y = (map(int,point))
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из координат')
            continue
        if f[x][y] != '*':
            print('Клетка занята')
            continue
        break
    return x,y

def winnner(f, user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

count = 0
while True:
    if count == 9:
        print('Ничья')
        break
    if count %2 == 0:
        user = 'x'
    else:
        user = 'o'
    show_box(box)
    x,y=player_input(box)
    box[x][y] = user
    if winnner(box, user):
        print(f"Выйграл {user}")
        show_box(box)
        break
    count += 1







