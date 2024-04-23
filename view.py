import tkinter as tk
import time
import random
from PIL import Image, ImageTk
SIZE = 30
WIDTH = 8 
HEIGH = 10 
MINES = 12
x_pos = 10
y_pos = 70 

#Matriz First Heigh then Width

class Game:
    def __init__(self):
        if (HEIGH * WIDTH) < MINES: return 
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.root.iconbitmap("assets/Minesweeper_1992.ico")
        self.root.geometry("280x380+1100+200")

        self.planted_mines = tk.Frame(self.root,bg="#AFA8A8")
        self.planted_mines.place(x=10,y=10,width=90,height=50)

        self.mines_remain = tk.Label(self.planted_mines,font=('digital-7',30,'bold'),
            background='black',foreground='red',text=MINES)
        self.mines_remain.pack()

        self.restart_button = tk.Button(self.root,text="(ツ)")
        self.restart_button.place(x=110,y=10,height=50,width=50)

        self.time = tk.Frame(self.root,bg="#AFA8A8")
        self.time.place(x=170,y=10,width=90,height=50)

        self.lbl_time = tk.Label(self.time,font=('digital-7',30,'bold'),
            background='black',foreground='red')
        self.lbl_time.pack()

        self.board = tk.Frame(self.root,bg="#AFA8A8")
        self.board.place(x=10,y=70,height=300,width=250)
     
        only_bombs_matriz,mines_place = self.game_matriz()

        matriz_game = self.check_matriz(only_bombs_matriz)
    
        
        for i in range(HEIGH):
            print(matriz_game[i])
        print(mines_place)
        
        for y in range(HEIGH):
            for x in range(WIDTH):
               Celda(self.root,(x_pos+(SIZE*x)),(y_pos+(SIZE*y)),matriz_game[y][x],x,y)
                
                  
                 

       
        self.root.mainloop()

    def mines_position(self):
        mines_place = []
        for i in range(MINES):
            while True:
                x = random.randint(0,(WIDTH - 1))
                y =random.randint(0,(HEIGH - 1))
                mines_place.append([y,x])
                if i == mines_place.index([y,x]):
                    break
                else:
                    mines_place.pop(i)
        return mines_place


    def game_matriz(self):
        matriz = []
        for i in range(HEIGH):
            matriz.append([0]*WIDTH)
        mines_place = self.mines_position()
        for val in mines_place:
            x = val[0]
            y = val[1]
            matriz[x][y] = 9
        return matriz,mines_place
        

    def around(self,x,y):
        around = []
        to_remove = []
        around.append([(y-1),(x-1)])
        around.append([(y-1),(x)])
        around.append([(y-1),(x+1)])
        around.append([(y),(x-1)])
        around.append([(y),(x+1)])
        around.append([(y+1),(x-1)])
        around.append([(y+1),(x)])
        around.append([(y+1),(x+1)])
        for val in around:
            if val[0]==-1 or val[1]==-1 or (val[0]>=HEIGH) or (val[1]>=WIDTH):
                to_remove.append(val)
        for rem in to_remove:
            around.remove(rem)
        return  around

    def bombs_around(self,matriz,y,x):
        bombs = 0
        if matriz[y][x] == 9:
            return matriz
        else:
            around_val =self.around(x,y)
            for val in around_val:
                if matriz[val[0]][val[1]]==9:
                    bombs = bombs + 1
            matriz[y][x] = bombs
            return matriz
        
    def check_matriz(self,matriz):
        for y in range(HEIGH):
            for x in range(WIDTH):
                matriz = self.bombs_around(matriz,y,x) 
        return matriz
    


class Celda:
    def __init__(self,frame,x,y,val,mat_x,mat_y):
        self.frame = frame
        self.val = val
        self.x = x
        self.y = y
        self.mat_x = mat_x
        self.mat_y = mat_y
        self.photo = self.image("assets/unopened.png")
        self.button = tk.Button(self.frame,image=self.photo,command=lambda :self.click())
        self.button.bind("<Button-3>",lambda x:self.red_flag())
        self.button.place(x=self.x,y=self.y,height=SIZE,width=SIZE)
        

    def get_val(self):
        return self.val  

    def click(self):
        if self.val == 9:
            self.photo = self.image("assets/mine_revealed.png")
            self.button.config(image=self.photo)
               
        elif self.val == 0:
            self.photo = self.image("assets/blank.png")
            self.button.config(image=self.photo)
            #self.flood_fill(self.mat_y,self.mat_x)
            
             
        else:
            self.photo = self.image(f"assets/{self.val}.png")
            self.button.config(image=self.photo)
            
        del self.button
        self.result = tk.Label(self.frame,image=self.photo)
        self.result.place(x=self.x,y=self.y,height=SIZE,width=SIZE)    
        return self.val
        
    def red_flag(self):
        self.photo = self.image("assets/redflag.png")
        self.button.config(image=self.photo,state="disabled")
        self.button.bind("<Button-3>",lambda x:self.unopened())
        

    def unopened(self):
        self.photo = self.image("assets/unopened.png")
        self.button.config(image=self.photo,state="normal")
        self.button.bind("<Button-3>",lambda x:self.red_flag())

    def game_over(self):
        return False
    
    def continuar(self):
        return True
    
    def image(self,img_route):
        my_img_pc = Image.open(img_route)
        resize_pc=my_img_pc.resize((SIZE,SIZE))
        photo_pc = ImageTk.PhotoImage(resize_pc)
        return photo_pc
    
    
        
            
            
    
            

        


Game()
