import tkinter as tk
from PIL import Image, ImageTk

class Celda:
    def __init__(self,frame,x,y,val):
        self.frame = frame
        self.val = val
        self.x = x
        self.y = y
        self.photo = self.image("assets/unopened.png")
        self.button = tk.Button(self.frame,image=self.photo,command=lambda :self.click())
        self.button.bind("<Button-3>",lambda x:self.red_flag())
        self.button.place(x=self.x,y=self.y,height=50,width=50)
        

    def get_val(self):
        return self.val  

    def click(self):
        if self.val == 9:
            self.photo = self.image("assets/mine_revealed.png")
            self.button.config(image=self.photo)
           
            
        elif self.val == 0:
            self.photo = self.image("assets/blank.png")
            self.button.config(image=self.photo)
            
            
        else:
            self.photo = self.image(f"assets/{self.val}.png")
            self.button.config(image=self.photo)
        del self.button
        self.result = tk.Label(self.frame,image=self.photo)
        self.result.place(x=self.x,y=self.y,height=50,width=50)
        
            
        
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
        resize_pc=my_img_pc.resize((50,50))
        photo_pc = ImageTk.PhotoImage(resize_pc)
        return photo_pc
    




