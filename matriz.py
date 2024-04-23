import random
from celda import Celda
HEIGH = 8   
WIDHT = 14
MINES = 20


def mines_position():
    mines_place = []
    for i in range(MINES):
        while True:
            x = random.randint(0,(WIDHT-1))
            y =random.randint(0,(HEIGH-1))
            mines_place.append([x,y])
            if i == mines_place.index([x,y]):
                break
            else:
                mines_place.pop(i)
    return mines_place


def game_matriz(view = False):
    matriz = []
    for i in range(WIDHT):
        matriz.append([0]*HEIGH)
    if view:
        for x in range(WIDHT):
            for y in range(HEIGH):
                matriz[x][y] = "??" 
        return matriz  
    else:
        mines_place = mines_position()
        for val in mines_place:
            x = val[0]
            y = val[1]
            matriz[x][y] = 9
        return matriz,mines_place
    

def around(x,y):
    around = []
    to_remove = []
    around.append([(x-1),(y-1)])
    around.append([(x-1),(y)])
    around.append([(x-1),(y+1)])
    around.append([(x),(y-1)])
    around.append([(x),(y+1)])
    around.append([(x+1),(y-1)])
    around.append([(x+1),(y)])
    around.append([(x+1),(y+1)])
    for val in around:
        if val[0]==-1 or val[1]==-1 or (val[0]>=HEIGH) or (val[1]>=WIDHT) or (val[0]>=WIDHT) or (val[1]>=HEIGH) :
            to_remove.append(val)
    for rem in to_remove:
        around.remove(rem)
    return  around

def bombs_around(matriz,x,y):
    bombs = 0
    if matriz[x][y] == 9:
        return matriz
    else:
        around_val =around(x,y)
        for val in around_val:
            if matriz[val[0]][val[1]]==9:
                bombs = bombs + 1
        matriz[x][y] = bombs
        return matriz
    
def check_matriz(matriz):
    for x in range(WIDHT):
        for y in range(HEIGH):
            matriz = bombs_around(matriz,x,y) 
    return matriz

def game_over():
    print("Se terminó el juego")

def flood_fill(y,x):
    if x==-1 or y==-1 or (y>=HEIGH) or (x>=WIDHT) or (x>=HEIGH) or (y>=WIDHT):
        return
    celda_vista = Celda(view_matriz[y][x]).get_val()
    celda_juego = Celda(matriz_game[y][x]).get_val()
    if celda_vista == "??" and (celda_juego != 9 and celda_juego !=0):
        view_matriz[y][x] = f"{matriz_game[y][x]} "
    if celda_vista == "??" and celda_juego == 0 :
        view_matriz[y][x] = f"{matriz_game[y][x]} "
        flood_fill(y-1,x)
        flood_fill(y-1,x+1)
        flood_fill(y,x+1)
        flood_fill(y+1,x+1)
        flood_fill(y+1,x)
        flood_fill(y+1,x-1)
        flood_fill(y,x-1)
        flood_fill(y-1,x-1)

def check_mines_in_game(matriz):
    count_in_game = 0
    for x in range(WIDHT):
        for y in range(HEIGH):
            if matriz[x][y] == "XX":
                count_in_game +=1
    return count_in_game

def check_all_cleared_mines(mines_place,view_matriz,matriz_game):
    for i in mines_place:
        if (view_matriz[i[0]][i[1]] == "XX") and (matriz_game[i[0]][i[1]] == 9):
            continue
        else:
            return False
    return True

           

    


view_matriz = game_matriz(True)       
only_bombs_matriz,mines_place = game_matriz()
matriz_game = check_matriz(only_bombs_matriz)

for i in range(HEIGH):
    print(matriz_game[i])


while False:

    print("------------------Game----------------------")
    mined = check_mines_in_game(view_matriz)
    
    if mined == MINES:
        if check_all_cleared_mines(mines_place,view_matriz,matriz_game):
            print("Felicidades Ganaste!!!!")
            for i in range(HEIGH):
                print(matriz_game[i])
            break
    
    
    print(f"Minas Puestas: {mined} --- Minas Restantes: {MINES-mined}")
    coordenanda = []
    for w in range(WIDHT):
        if len(str(w))==1:
            coordenanda.append(f"0{w}")
        else:
            coordenanda.append(f"{w}")
    print(f"[X] {coordenanda}")
    for i in range(HEIGH):
        if len(str(i))==1:
            print(f"0{i}  {view_matriz[i]}")
        else:
            print(f"{i}  {view_matriz[i]}")
    try:
        x = int(input("Selecciona el Valor Horizontal: "))
        y = int(input("Selecciona el valor Vertical: "))
    except:
        continue
    if x>=WIDHT:
        continue
    if y>=HEIGH:
        continue

    print("Menú: ")
    print("1-Plantar Mina:")
    print("2-Click:")
    print("3-Salir:")
    try:
        res = int(input("Selecciona un valor: "))
    except:
        continue
    if res == 1:
        if view_matriz[y][x] == "XX":
            view_matriz[y][x] = "??"
        else:
            view_matriz[y][x] = "XX"
    elif res == 2:
        if Celda(matriz_game[y][x]).click():
            if matriz_game[y][x] == 0:
                flood_fill(y,x)
            else:
                view_matriz[y][x] = f"{matriz_game[y][x]} "
        else:
            game_over()
            break
    
    elif res == 3:
        print("Saliendo del Juego:")
        break
    
    else:
        continue

        





