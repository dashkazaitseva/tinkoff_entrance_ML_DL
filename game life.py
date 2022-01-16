import numpy as np
import time

class Cell:
    def __init__(self, alive = False):
        self.alive = alive
    def __str__(self):
        if self.alive:
            return '*'
        return '.'


class Field:
    def __init__(self, size: tuple[int, int], input_data: list):
        self.size = (size[0] + 4, size[1] + 4)
        self.field =[[Cell(0) for j in range(self.size[1])] for i in range(self.size[0])]
        if (len(input_data) != size[0]):
            for i in range(size[0]):
                for j in range(size[1]):
                    self.field[i + 2][j + 2] = Cell(np.random.randint(2))
        else:
            for i in range(size[0]):
                for j in range(size[1]):
                    self.field[i + 2][j + 2] = Cell(input_data[i][j]) 

    def gen_new_field(self):
        new_field = Field((self.size[0] - 4, self.size[1] - 4), [[0 for j in range(self.size[1] - 4)] for i in range(self.size[0] - 4)])
        for i in range(1, self.size[0] - 1):
            for j in range(1, self.size[1] - 1):
                cnt = 0
                cnt += self.field[i - 1][j - 1].alive
                cnt += self.field[i - 1][j].alive
                cnt += self.field[i - 1][j + 1].alive
                cnt += self.field[i][j - 1].alive
                cnt += self.field[i][j + 1].alive
                cnt += self.field[i + 1][j - 1].alive
                cnt += self.field[i + 1][j].alive
                cnt += self.field[i + 1][j + 1].alive
                
                if ((self.field[i][j]).alive and 2 <= cnt <= 3):
                    new_field.field[i][j] = Cell(1)
                if (not (self.field[i][j]).alive and cnt == 3):
                    new_field.field[i][j] = Cell(1)
                    
        #проверка, не нужно ли поле побольше
        cell_on_border = False
        for i in [1, self.size[0] - 2]:
            for j in [1, self.size[1] - 2]:
                if ((new_field.field[i][j]).alive):
                    cell_on_border = True
        if (cell_on_border):
            self.field = new_field
            new_field = field((self.size[0] + 2, self.size[1] + 2), [[0 for j in range(self.size[1] + 2)] for i in range(self.size[0] + 2)])
            for i in range(self.field.size[0]):
                for j in range(self.field.size[1]):
                    new_field[i + 1][j + 1] = self.field[i][j]
            self.size = (self.size[0] + 2, self.size[1] + 2)

        return new_field
        

    def __str__(self):
        с = [''.join([str(self.field[i][j]) for j in range(self.size[1])]) for i in range(self.size[0])]
        return "\n".join(с)

    

class Game_of_life: #игра
    def __init__(self, size: tuple[int, int], input_field: Field) -> None: #инициализация
        self.rows, self.cols = size
        self.history = set() #будем хранить историческую выкладку поля
        self.current_field = Field(size,input_field)

    def continue_game(self): #проверка нужно ли продолжать
        for el in self.history:
            f1 = el.field
            f2 = self.current_field.field
            if len(f1) == len(f2) and len(f1[0]) == len(f2[0]):
                ans = False
                for i in range(len(f1)):
                    for j in range(len(f2)):
                        if f1[i][j].alive != f2[i][j].alive:
                            ans = True
                if not ans:
                    return False
        return True
    def play(self) -> None: #игра
        cont = True
        while cont:
            print(self.current_field)
            self.history.add(self.current_field)
            self.current_field = self.current_field.gen_new_field()
            cont = self.continue_game()
            time.sleep(3)



Game_of_life((2, 2), [[1, 0], [1, 1]]).play()


    
    
        
        
