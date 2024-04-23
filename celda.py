class Celda:
    def __init__(self,val):
        self.val = val

    def get_val(self):
        return self.val  

    def click(self):
        if self.val == 9:
            val = self.game_over()
            return val
        else:
            val = self.continuar()
            return val

    def game_over(self):
        return False
    
    def continuar(self):
        return True
    
