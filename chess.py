import os
class Figure:
    figure: str
    color: str
    pos_X: int
    pos_Y: int
    icon: str

    icons = {('Pawn', 'White'): '♙',
             ('Queen', 'White'): '♕',
             ('Rook', 'White'): '♖︎',
             ('Bishop', 'White'): '♗',
             ('Knight', 'White'): '♘︎',
             ('King', 'White'): '♔︎',
             ('Pawn', 'Black'): '♟︎',
             ('Queen', 'Black'): '♛︎',
             ('Rook', 'Black'): '♜︎',
             ('Bishop', 'Black'): '♝︎',
             ('Knight', 'Black'): '♞︎',
             ('King', 'Black'): '♚︎'}

    def __init__(self, figure, color, pos_X, pos_Y):
        self.figure = figure
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.icon = self.icons[(figure, color)]
WPawn0 = Figure('Pawn', 'White', 0, 1)
WPawn1 = Figure('Pawn', 'White', 1, 1)
WPawn2 = Figure('Pawn', 'White', 2, 1)
WPawn3 = Figure('Pawn', 'White', 3, 1)
WPawn4 = Figure('Pawn', 'White', 4, 1)
WPawn5 = Figure('Pawn', 'White', 5, 1)
WPawn6 = Figure('Pawn', 'White', 6, 1)
WPawn7 = Figure('Pawn', 'White', 7, 1)
# _______________________________________________________________
BPawn0 = Figure('Pawn', 'Black', 0, 6)
BPawn1 = Figure('Pawn', 'Black', 1, 6)
BPawn2 = Figure('Pawn', 'Black', 2, 6)
BPawn3 = Figure('Pawn', 'Black', 3, 6)
BPawn4 = Figure('Pawn', 'Black', 4, 6)
BPawn5 = Figure('Pawn', 'Black', 5, 6)
BPawn6 = Figure('Pawn', 'Black', 6, 6)
BPawn7 = Figure('Pawn', 'Black', 7, 6)
# _______________________________________________________________
WRook0 = Figure('Rook', 'White', 0, 0)
WRook1 = Figure('Rook', 'White', 7, 0)
WKnight0 = Figure('Knight', 'White', 1, 0)
WKnight1 = Figure('Knight', 'White', 6, 0)
WBishop0 = Figure('Bishop', 'White', 2, 0)
WBishop1 = Figure('Bishop', 'White', 5, 0)
WKing = Figure('King', 'White', 3, 0)
WQueen = Figure('Queen', 'White', 4, 0)
# _______________________________________________________________
BRook0 = Figure('Rook', 'Black', 0, 7)
BRook1 = Figure('Rook', 'Black', 7, 7)
BKnight0 = Figure('Knight', 'Black', 1, 7)
BKnight1 = Figure('Knight', 'Black', 6, 7)
BBishop0 = Figure('Bishop', 'Black', 2, 7)
BBishop1 = Figure('Bishop', 'Black', 5, 7)
BKing = Figure('King', 'Black', 3, 7)
BQueen = Figure('Queen', 'Black', 4, 7)
Figures = [WPawn0, WPawn1, WPawn2, WPawn3, WPawn4, WPawn5, WPawn6, WPawn7, BPawn7, BPawn6, BPawn5, BPawn4,
               BPawn3, BPawn2, BPawn1, BPawn0, WRook0, WRook1, WKnight1, WKnight0, WBishop0, WBishop1, WKing, WQueen,
               BRook1, BRook0, BBishop1, BBishop0, BKnight1, BKnight0, BKing, BQueen]


def ladya(ladya1:Figure, z, w):
    x = ladya1.pos_X
    y = ladya1.pos_Y
    if x == z or y == w:
        return True
    else:
        return False
    
def king(king1:Figure, z, w):
    x = king1.pos_X
    y = king1.pos_Y
    if abs(x - z) <= 1 and abs(y - w) <= 1:
        return True
    else:
        return False

def slon(slon1:Figure, z, w):
    x = slon1.pos_X
    y = slon1.pos_Y
    if x + z == y + w or abs(x - z) == abs(y - w):
        return True
    else:
        return False
    
def ferz(ferz1:Figure, z, w):
    x = ferz1.pos_X
    y = ferz1.pos_Y
    if x == z or y == w:
        return True
    elif x + y == z + w or y - x == w - z:
        return True
    else:
        return False

def horse(horse1:Figure, z, w):
    x = horse1.pos_X
    y = horse1.pos_Y
    if (w == y + 2 or w == y - 2) and (z == x + 1 or z == x - 1):
        return True
    elif (w == y + 1 or w == y - 1) and (z == x + 2 or z == x - 2):
        return True
    else:
        return False

def pawn(pawn1:Figure, z, w, Figures):
    field = update_field1(Figures)
    x = pawn1.pos_X
    y = pawn1.pos_Y
    k = pawn1.color
    if pawn1.color == 'Black':
        if y == w + 1 and x == z and field[w][z] == 0:
            return True
        elif field[w][z] != 0 and ((x == z + 1 and y == w + 1) or (x == z - 1 and y == w + 1)):
             for elem in Figures:
                 if elem.pos_X == z and elem.pos_Y == w:
                     if elem.color != k:
                         if elem.figure != 'King':
                             Figures.remove(elem)
                             return True
                         elif elem.figure == 'King':
                             return True
        else:
            return False
    elif pawn1.color == 'White':
        if y == w - 1 and x == z and field[w][z] == 0:
            return True
        elif field[w][z] != 0  and ((y == w - 1 and x == z + 1) or (x == z - 1 and y == w - 1)):
             for elem in Figures:
                 if elem.pos_X == z and elem.pos_Y == w:
                     if elem.color != k:
                         Figures.remove(elem)
                         return True
                     elif elem.figure == 'King':
                             return True
        else:
            return False

def update_field1(Figures):
        field = [[0] * 8 for i in range(8)]
        for elem in Figures:
            x_update = elem.pos_X
            y_update = elem.pos_Y
            field[y_update][x_update] = elem.icon
        return field
    
def update_field(field):
    field = update_field1(field)
    for i in field:
        print(*i)
        
def can_go(z, w, figure):
    figure = figure
    z = z
    w = w
    field = update_field1(Figures)
    x = figure.pos_X
    y = figure.pos_Y
    k = []
    if z >= 8 or w >= 8:
        return False
    else:
        while x != z or y != w:
            if x > z and y > w:
                x = x - 1
                y = y - 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif x < z and y < w:
                x = x + 1
                y = y + 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif y > w and x < z:
                x = x + 1
                y = y - 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif y < w and x > z:
                x = x - 1
                y = y + 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif x == z and y > w:
                y = y - 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif y < w and x == z:
                y = y + 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif x > z and y == w:
                x = x - 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
            elif x < z and y == w:
                x = x + 1
                if field[y][x] != 0:
                    k.append(y)
                    k.append(x)
    for i in range(len(k) - 1):
        if k[i] == w and k[i + 1] == z and len(k) == 2:
            check = attack(z, w, Figures, figure)
            if check == True:
                return True
            else:
                return False
    if len(k) == 0:
        return True
    
def attack(z, w, Figures, Figure):
    k = Figure.color
    field = update_field1(Figures)
    if field[w][z] != 0:
        for elem in Figures:
            if elem.pos_X == z and elem.pos_Y == w:
                if elem.color != k and (ladya(elem, z, w) == True or king(elem, z, w) == True or slon(elem, z, w) == True or ferz(elem, z, w) == True):
                    if elem.figure != 'King':
                        Figures.remove(elem)
                        return True
                    elif elem.figure == 'King':
                             return True
    else:
        return False
def horseattack(z, w, Figures, Figure):
    k = Figure.color
    field = update_field1(Figures)
    if field[w][z] != 0:
        for elem in Figures:
            if elem.pos_X == z and elem.pos_Y == w:
                if elem.color != k and horse(Figure, z, w) == True:
                    if elem.figure != 'King':
                        Figures.remove(elem)
                        return True
                    elif elem.figure == 'King':
                             return True
    elif field[w][z] == 0:
        return True
    else:
        return False
def strchange(figure):
    figure = figure.title()
    alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    if figure[0] in alfa and len(figure) == 2:
        for i in range(len(alfa)):
            if figure[0] == alfa[i]:
                z = str(i)
        if figure[-1].isdigit() == True and int(figure[-1]) > 0 and int(figure[-1]) < 9:
            a = int(figure[-1]) - 1
            a = str(a)
            z = (z + a)
            return z
    else:
        return False

def get_figure(z, w):
    for elem in Figures:
        x = elem.pos_X
        y = elem.pos_Y
        if x == z and y == w:
            return elem
    else:
        return 0
def shach(Figures, figure2):
    status = []
    z = figure2.pos_X
    w = figure2.pos_Y
    for elem in Figures:
        if elem.figure != 'Knight' and elem.figure != 'Pawn' and elem.color != figure2.color:
            if can_go(z, w, elem) == True and (ladya(elem, z, w) == True or king(elem, z, w) == True or slon(elem, z, w) == True or ferz(elem, z, w) == True):
                status.append(1)
        elif elem.figure == 'Knight' and elem.color != figure2.color:
            if horseattack(z, w, Figures, elem) == True and horse(elem, z, w) == True:
                status.append(1)
        elif elem.figure == 'Pawn' and elem.color != figure2.color:
            if pawn(elem, z, w, Figures) == True:
                status.append(1)
        else:
            status.append(0)
    if 1 in status:
        return 'Шах'
    else:
        return 'Ok'
def kinggo(figure, Figures):
    counter = 0
    while counter < 1:
        if figure.color == 'Black' and shach(Figures, figure) == 'Шах':
            print('Ходите чёрным королём или другой фигурой, шах ')
            pos = input()
            pos = strchange(pos)
            print("Выберите новую позицию")
            new_pos = input()
            new_pos = strchange(new_pos)
            if  (pos != False and new_pos != False) and (pos != None and new_pos != None):
                state = get_figure(int(pos[0]), int(pos[1]))
                if state == 0:
                    print('Выберите верную позицию фигры')
                elif pos == new_pos:
                    print('Нельзя стоять на месте')
                elif state.color == 'Black':
                    if state.figure == 'Pawn':
                        funk = pawn(state, int(new_pos[0]), int(new_pos[1]), Figures)
                        if funk == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])   
                            counter += 1
                    if state.figure == 'Knight':
                        funk = horse(state, int(new_pos[0]), int(new_pos[1]))
                        horsecheck = horseattack(int(new_pos[0]), int(new_pos[1]), Figures, state)
                        if funk == True and horsecheck == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'Queen':
                        funk = ferz(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'King':
                        funk = king(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'Rook':
                        funk = ladya(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'Bishop':
                        funk = slon(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                if counter == 0 or shach(Figures, figure) == 'Шах':
                    print('Сделайте правильный ход')
                    state.pos_X = int(pos[0])
                    state.pos_Y = int(pos[1])
                    counter = 0
            else:
                print('Выберите верную координату')
                
        elif figure.color == 'White' and shach(Figures, figure) == 'Шах':
            print('Ходите белым королём, шах')
            pos = input()
            pos = strchange(pos)
            print("Выберите новую позицию")
            new_pos = input()
            new_pos = strchange(new_pos)
            if  (pos != False and new_pos != False) and (pos != None and new_pos != None):
                state = get_figure(int(pos[0]), int(pos[1]))
                if state == 0:
                    print('Выберите верную позицию фигры')
                elif pos == new_pos:
                    print('Нельзя стоять на месте')
                elif state.color == 'White':
                    if state.figure == 'Pawn':
                        funk = pawn(state, int(new_pos[0]), int(new_pos[1]), Figures)
                        if funk == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])   
                            counter += 1
                    if state.figure == 'Knight':
                        funk = horse(state, int(new_pos[0]), int(new_pos[1]))
                        horsecheck = horseattack(int(new_pos[0]), int(new_pos[1]), Figures, state)
                        if funk == True and horsecheck == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'Queen':
                        funk = ferz(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'King':
                        funk = king(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'Rook':
                        funk = ladya(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                    if state.figure == 'Bishop':
                        funk = slon(state, int(new_pos[0]), int(new_pos[1]))
                        go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                        if funk == True and go == True:
                            state.pos_X = int(new_pos[0])
                            state.pos_Y = int(new_pos[1])
                            counter += 1
                if counter == 0 or shach(Figures, figure) == 'Шах':
                    print('Сделайте правильный ход')
                    state.pos_X = int(pos[0])
                    state.pos_Y = int(pos[1])
                    counter = 0
            else:
                print('Выберите верную координату')
    
def print_battlefield(Figures):
        field = update_field1(Figures)
        print('┌────┬────┬────┬────┬────┬────┬────┬────┬────┐')
        print('│    │ A  │ B  │ C  │ D  │ E  │ F  │ G  │ H  │')
        print('├────┼────┼────┼────┼────┼────┼────┼────┼────┤')
        i = 0
        for line in field:
            i += 1
 
            print('│ ' + str(i) + '  │', end='')
 
            for symbl in line:
                if symbl == '♗':
                    symbl = '♗' + ' '
                elif symbl == '♕':
                    symbl = '♛' + ' '
                elif symbl == '♙':
                    symbl = '♙' + ' '
                elif symbl == 0:
                    symbl = '  '
 
                to_print = ' ' + symbl + ' '
 
                print(to_print, end='│')
 
            print(' ')
 
            if i != 8:
                print('├────┼────┼────┼────┼────┼────┼────┼────┼────┤')
            else:
                print('└────┴────┴────┴────┴────┴────┴────┴────┴────┘')

    
        
def gameWhite():
    counter = 0
    while counter < 1:
        counter = 0
        print("Выберите фигуру")
        pos = input()
        pos = strchange(pos)
        print("Выберите новую позицию")
        new_pos = input()
        new_pos = strchange(new_pos)
        if (pos != False and new_pos != False) and (pos != None and new_pos != None):
            state = get_figure(int(pos[0]), int(pos[1]))
            if state == 0:
                print('Выберите верную позицию фигры')
            elif pos == new_pos:
                print('Нельзя стоять на месте')
            elif state.color == 'White':
                if state.figure == 'Pawn':
                    funk = pawn(state, int(new_pos[0]), int(new_pos[1]), Figures)
                    if funk == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])   
                        counter += 1
                if state.figure == 'Knight':
                    funk = horse(state, int(new_pos[0]), int(new_pos[1]))
                    horsecheck = horseattack(int(new_pos[0]), int(new_pos[1]), Figures, state)
                    if funk == True and horsecheck == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'Queen':
                    funk = ferz(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'King':
                    funk = king(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'Rook':
                    funk = ladya(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'Bishop':
                    funk = slon(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if counter == 0 or shach(Figures, WKing) == 'Шах':
                    print('Сделайте правильный ход')
                    state.pos_X = int(pos[0])
                    state.pos_Y = int(pos[1])
                    counter = 0
            else:
                print('Выберите белую фигуру')
        else:
            print('Выберите верную координату')
                
def gameBlack():
    counter = 0
    while counter < 1:
        counter = 0
        print("Выберите фигуру")
        pos = input()
        pos = strchange(pos)
        print("Выберите новую позицию")
        new_pos = input()
        new_pos = strchange(new_pos)
        if (pos != False and new_pos != False) and (pos != None and new_pos != None):
            state = get_figure(int(pos[0]), int(pos[1]))
            if state == 0:
                print('Выберите верную позицию фигры')
            elif pos == new_pos:
                print('Нельзя стоять на месте')
            elif state.color == 'Black':
                if state.figure == 'Pawn':
                    funk = pawn(state, int(new_pos[0]), int(new_pos[1]), Figures)
                    if funk == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])   
                        counter += 1
                if state.figure == 'Knight':
                    funk = horse(state, int(new_pos[0]), int(new_pos[1]))
                    horsecheck = horseattack(int(new_pos[0]), int(new_pos[1]), Figures, state)
                    if funk == True and horsecheck == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'Queen':
                    funk = ferz(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'King':
                    funk = king(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'Rook':
                    funk = ladya(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if state.figure == 'Bishop':
                    funk = slon(state, int(new_pos[0]), int(new_pos[1]))
                    go = can_go(int(new_pos[0]), int(new_pos[1]), state)
                    if funk == True and go == True:
                        state.pos_X = int(new_pos[0])
                        state.pos_Y = int(new_pos[1])
                        counter += 1
                if counter == 0 or shach(Figures, BKing) == 'Шах':
                    print('Сделайте правильный ход')
                    state.pos_X = int(pos[0])
                    state.pos_Y = int(pos[1])
                    counter = 0
            else:
                print('Выберите чёрную фигуру')
        else:
            print('выберите верную координату')

def game(Figures):
    s = 0
    while True:
        os.system('cls')
        print_battlefield(Figures)
        s += 1
        if s % 2 != 0:
            print('Ход белых')
            if shach(Figures, WKing) != 'Шах':
                gameWhite()
            else:
                kinggo(WKing, Figures)
        elif s % 2 == 0:
            print('Ход чёрных')
            if shach(Figures, BKing) != 'Шах':
                gameBlack()
            else:
                kinggo(BKing, Figures)
    print('Игра окончена')

game(Figures)