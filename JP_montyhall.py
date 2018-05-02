import numpy as np 
from random import shuffle

#funcion que plantea las puertas de manera aleatoria para simular el t0 del jugador
def sort_doors():
 	lista = ["goat","goat","car"]
	np.random.shuffle(lista)
	return lista 

#funcion que escoje una puerta aleatoria como lo haria el jugador en el t1
def choose_door():
	num= [0,1,2]
	return np.random.choice(num)
	
#funcion que revela una cabra en una de las puertas despues de la eleccion del jugador
def reveal_door(lista,choice):

	for i in range (len(lista)):
		if((choice != i) & (lista[i] == "goat")):
			lista[i] = "GOAT_MONTY"
			return lista

#funcion que simula la decision del jugador sobre cambiarse o no de puerta. 
def finish_game(lista,choice,change):
	if(change == False):
		return lista[choice]
	else: 
		for i in range(len(lista)): 
			if((i != choice) & (lista[i]!= "GOAT_MONTY")):	
				return lista[i]

#Se simula 100 veces para mirar ambos escenarios para ver si cambia segun la probabilidad bayesiana. 
lista_true=[]
lista_false=[]

for i in range(100): 
	numero = choose_door()	
	lista_true.append(finish_game(reveal_door(sort_doors(), numero), numero , True))	
	lista_false.append(finish_game(reveal_door(sort_doors(), numero), numero , False))	

contador = 0
for i in range (len(lista_true)): 
 
	if(lista_true[i] == "car"):
		contador= contador+ 1  	
		
print "la probabilidad de ganar cambiando es:", contador,"%"

contador1 = 0 
for i in range(len(lista_false)):
	
	if(lista_false[i] == "car"):
		contador1 = contador1+1
	
print "la probabilidad de ganar no cambiando la puerta es:", contador1,"%"




 



