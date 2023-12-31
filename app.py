import random, sys, getch, os, time

class MyClass:
    def __init__(self):
        self.winbreak = False
        self.cls = ""
        if sys.platform == "linux":
            self.cls = "clear"

        elif sys.platform == "win32":
            self.cls = "cls"

        self.user_symbol = "X"
        if len(sys.argv) > 1:
            self.user_symbol = sys.argv[1]
        
        self.ai_symbol = "o"
        if self.user_symbol in ["o","0","O"]:
            self.ai_symbol = "#"

        self.placeHolders = [[" "," "," "],
                            [" "," "," "],
                            [" "," "," "]
                            ]
        
        self.scheme =  [[1,2,3],
                        [4,5,6],
                        [7,8,9]
                        ]

    def output(self):
        print(f'''
\t GAME BOARD > \t\t INPUT VALUES >

\t{self.placeHolders[0][0]} | {self.placeHolders[0][1]} | {self.placeHolders[0][2]} \t\t {self.scheme[0][0]} | {self.scheme[0][1]} | {self.scheme[0][2]}
\t--------- \t\t ---------
\t{self.placeHolders[1][0]} | {self.placeHolders[1][1]} | {self.placeHolders[1][2]} \t\t {self.scheme[1][0]} | {self.scheme[1][1]} | {self.scheme[1][2]}
\t--------- \t\t ---------
\t{self.placeHolders[2][0]} | {self.placeHolders[2][1]} | {self.placeHolders[2][2]} \t\t {self.scheme[2][0]} | {self.scheme[2][1]} | {self.scheme[2][2]}
''')

    def get_user_input(self):
        position = input("Enter Position :: ")
        position = int(position)
        temp = 1
        for i in range(3):
            for j in range(3):
                if temp == position:
                    self.placeHolders[i][j] = self.user_symbol
                temp += 1
                
    def check_win(self):
        #checks if row's element are equal
        for i in range(3):
            if self.placeHolders[i][0] == self.placeHolders[i][1] and self.placeHolders[i][1] == self.placeHolders[i][2] and self.placeHolders[i][0] != " ":
                return 1,self.placeHolders[i][0]

        #checks if column's element are equal
        for i in range(3):
            if self.placeHolders[0][i] == self.placeHolders[1][i] and self.placeHolders[1][i] == self.placeHolders[2][i] and self.placeHolders[0][i] != " ":
                return 1,self.placeHolders[0][i]

        #checks if diagonal elements are equal
        if self.placeHolders[0][0] == self.placeHolders[1][1] and self.placeHolders[1][1] == self.placeHolders[2][2] and self.placeHolders[0][0] != " ":
            return 1,self.placeHolders[0][0]
        if self.placeHolders[0][2] == self.placeHolders[1][1] and self.placeHolders[1][1] == self.placeHolders[2][0] and self.placeHolders[2][0] != " ":
            return 1,self.placeHolders[0][2]

        return 0,0
        
    def ai_input(self):
        #checks if ai can win
        for i in range(3):
            for j in range(3):
                if self.placeHolders[i][j] == " ":
                    self.placeHolders[i][j] = self.ai_symbol
                    if self.check_win()[0] == 1:   # ai wins
                        return
                    else:
                        self.placeHolders[i][j] = " "

        #ai checks on what position user can win and use its move on that position to block user win
        for i in range(3):
            for j in range(3):
                if self.placeHolders[i][j] == " ":
                    self.placeHolders[i][j] = self.user_symbol
                    if self.check_win()[0] == 1:   # user wins
                        self.placeHolders[i][j] = self.ai_symbol # blocks user win
                        return
                    else:
                        self.placeHolders[i][j] = " "
                    
        # enters symbol at random position
        if len(self.is_empty()) > 0 :
            temp = self.is_empty()
            x = random.choice(temp)
            y = 1
            print(temp)
            for i in range(3):
                for j in range(3):
                    if y == x:
                        self.placeHolders[i][j] = self.ai_symbol
                        return
                    y += 1

    def is_empty(self):
        temp = []
        x = 1
        for i in range(3):
            for j in range(3):
                if self.placeHolders[i][j] == " ":
                    temp.append(x)
                x += 1
        return temp
        
    def print_win(self):
        if self.check_win()[0] == 1:
            if self.check_win()[1] == self.ai_symbol:
                os.system(self.cls)
                self.output()              
                print("AI WON")
                sys.exit()
            elif self.check_win()[1] == self.user_symbol:
                os.system(self.cls)
                self.output()
                print("USER WON")
                sys.exit()
                
    def exec(self):
        while True:
            if len(self.is_empty()) == 0:
                os.system(self.cls)
                self.output()
                print("DRAW")
                sys.exit()
            os.system(self.cls)
            self.output()
            self.get_user_input()
            self.print_win()
            self.ai_input()
            self.print_win()
            
app = MyClass()
app.exec()
        
