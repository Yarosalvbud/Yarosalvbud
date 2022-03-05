class Lexer:
    def __init__(self):
        self.buffer = ""
        self.b_counter = 0
        self.current_state = "s"
        self.lexem = []
        self.end_m = ['+', '-', '*', '/', '^', '(']
        self.viraz = []



    def s_func(self, stroka):
        for symbol in range(len(stroka)):
            if stroka[symbol].isdigit():
                self.current_state = 'I'
                self.i_func(stroka[symbol])
            elif stroka[symbol] == '.':
                self.current_state = 'R'
                self.r_func(stroka[symbol])
            else:
                self.end_func(stroka[symbol])


    def i_func(self, symbol):
        if self.current_state == 'I':
            self.buffer += symbol

    def r_func(self, symbol):
        if self.current_state == 'R':
            self.buffer += symbol

    def end_func(self, symbol):
        if symbol in self.end_m:
            self.viraz.append(self.buffer)
            self.viraz.append(self.end_m[self.end_m.index(symbol)])
            self.buffer = ""

s = Lexer()
s.s_func('5.38+5')
print(s.viraz)
#Запускаем цикл в parse затем переходим в s_func которая распределит состояние и пришлёт ответ