# -*- coding: utf-8 -*-
import msvcrt

def concatenar(a,sep):                                  # Concatena los caracteres desde una lista
    return sep + sep.join(a) + sep

def dibujar_tb(a,b,c):
        l = concatenar(["_","_","_"]," ")               # Dibuja el tablero de juego 
        a = concatenar(a,"|")
        b = concatenar(b,"|")
        c = concatenar(c,"|")
        print (l,'\n'+ a,'\n'+ b,'\n' + c,'\n')

def casillas_tb():                                      # Dibuja el tablero de casillas numerico (referencia para ubicar X o O)
        f0 = ["1","2","3"]
        f1 = ["4","5","6"]
        f2 = ["7","8","9"]
        dibujar_tb(f0,f1,f2) 

def jugada(k):                                          # Realiza una jugada entera de un solo jugador: elige casilla válida y dibuja tablero actualizado
        casillas_tb()
        cond = 0

        while cond == 0:
                pos = input("{}: elija número de casilla a jugar entre 1 y 9: ".format(nombre[k]))

                if pos not in casillas:
                        print ("Elija una posición válida entre 1 y 9 ")            # Verificación de selección de casilla numero de 1 a 9
                        cond = 0

                else:
                        if pos in pos_jugadas:
                                print ("Casilla ocupada: elija otra ")              # Verificación de casilla libre para jugar
                                cond = 0
                        else: 
                                cond = 1                 
                                                                                                                            
        for i in range(3):                                                         # Dibuja simbolo en el tablero de juego (matriz) correspondiente con la casilla seleccionada
                for j in range(3):
                        if Tab[i][j] == pos: 
                                Tab[i][j] = simbolo[k]           
                                Tab_2[i][j] = simbolo[k]
                        else: 
                                continue

        pos_jugadas.append(pos)                 
        dibujar_tb(Tab_2[0],Tab_2[1],Tab_2[2])

def verificar(k):
        ganador = bool()
        if Tab_2[0][0] == simbolo[k] and Tab_2 [0][1] == simbolo[k] and Tab_2 [0][2] == simbolo[k]:                                     # Condicion ganar llenando primera fila cualquiera 
                ganador = True

        elif Tab_2[1][0] == simbolo[k] and Tab_2 [1][1] == simbolo[k] and Tab_2 [1][2] == simbolo[k]:                                   # Condicion ganar llenando segunda fila cualquiera 
                ganador = True

        elif Tab_2[2][0] == simbolo[k] and Tab_2 [2][1] == simbolo[k] and Tab_2 [2][2] == simbolo[k]:                                   # Condicion ganar llenando tercera fila cualquiera 
                ganador = True

        elif Tab_2[0][0] == simbolo[k] and Tab_2[1][0] == simbolo[k] and Tab_2[2][0] == simbolo[k]:                                   # Condicion ganar llenando primera columna 
                ganador = True

        elif Tab_2[0][1] == simbolo[k] and Tab_2[1][1] == simbolo[k] and Tab_2[2][1] == simbolo[k]:                                   # Condicion ganar llenando segunda columna 
                ganador = True
        
        elif Tab_2[0][2] == simbolo[k] and Tab_2[1][2] == simbolo[k] and Tab_2[2][2] == simbolo[k]:                                   # Condicion ganar llenando tercera columna 
                ganador = True

        elif Tab_2[0][0] == simbolo[k] and Tab_2[1][1] == simbolo[k] and Tab_2[2][2] == simbolo[k]:                                   # Condicion ganar llenado diagonal 1
                ganador = True

        elif Tab_2[0][2] == simbolo[k] and Tab_2[1][1] == simbolo[k] and Tab_2[2][0] == simbolo[k]:                                   # Condicion ganar llenado diagonal 2
                ganador = True
        
        else:
                ganador = False

        return ganador 


print ("JUEGO TA-TE-TI\n")                     
f = ["_","_","_"]                                       # Representación del tablero vacio
dibujar_tb(f,f,f)                                       

# Solicitar elegir simbolos válidos para los jugadores

simbolo = ["X","O"]
j1 = str()                                                 #simbolo del jugador 1 

while j1 not in simbolo:   
        j1 = str(input("Jugador 1: Elija simbolo 'X' u 'O': ")).upper()          
        
        if j1 == "X":
                j2 = "O"
                primero = "Jugador 1"                                
                print ("Jugador 1 juega con ", j1, "\nJugador 2 juega con ", j2, "\nComienza el juego el jugador 1\n")

        elif j1 == "O":
                j2 = "X"
                primero = "Jugador 2"
                print ("Jugador 1 juega con ", j1, "\nJugador 2 juega con ", j2, "\nComienza el juego el jugador 2\n")

        else: 
                print("Elija una opción válida")

if primero == "Jugador 1":                                                         # guarda en una lista los nombres de los jugadores en el orden correcto para jugar
        nombre = ["Jugador 1","Jugador 2"]
else:
        nombre = ["Jugador 2","Jugador 1"]

Tab = [["1","2","3"],["4","5","6"],["7","8","9"]]                                  # Casillas numericas como matriz de referencia 
Tab_2 = [["_","_","_"],["_","_","_"],["_","_","_"]]                                # Tablero del juego como matriz vacia
pos = 0                                                                            # variable referente a la posición a jugar en la tabla (1 a 9)
pos_jugadas = []                                                                   # lista donde se van guardando la posiciones ya jugadas
casillas = ["1","2","3","4","5","6","7","8","9"]                                   # lista de strings que representan las casillas para usar en funcion def "jugada"                     
turnos = [0,1,0,1,0,1,0,1,0]                                                       # lista de ordenada de los turnos máximos posibles en el juego

for k in turnos:                                                                   # Juega por turnos cada jugador y se verifica si hay ganador en cada jugada
        x = bool()
        jugada(k)

        if verificar(k) == True:                                                    # Se verifica si hay o no un ganador durante la jugada
                x = verificar(k)
                print("Gana {}".format(nombre[k]))
                break
        else:
                x == False
          
if x == False:                                                                     # Se verifica al completar todo el tablero un empate
        print("El juego termina en empate")
else:
        pass

msvcrt.getch()











