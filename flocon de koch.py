from turtle import* #importation de le bibliotèque turtle
from random import* #Pour la COULEUR !!!

speed(0)

def couleur(): #on choisit une couleur aléatoirement
  return choice(['red', 'blue', 'green', 'purple', 'violet', 'indigo', 'orange'])


def spirale():
  n = 10 #on définit la varriable n à 10
  for c in range (10) : #on fait 10 fois 2 forward n et left 90
    forward(n) #on avance de n
    left(90) #on tourne à gauche de 90 degrés
    forward(n) #on avance de n
    left(90)
    n = n + 10 #on augmente la variable n de 10

def rosace():
  for c in range (36): #j'ai tésté plusieurs fois en modifiant la boucle pour savoir que l'on doit la répéter 36 fois ni plus ni moins.
    circle(80) #on fait un cercle
    left(10) #on va décaler le cerle en changeant l'orientation

def creneau():
  for g in range (4): #on répète le tout 4 fois pour faire un grand carré
    for d in range (9): #on répète le tout pour faire une grande ligne crénelé
      forward(10)
      left(90)
      for k in range (2): #simplification pour ne pas écrire forward et right 2 fois
        forward(10)
        right(90)
      forward(10)
      left(90)
    backward(10)
    right(90) #on retourne de 10 en arrière et change de sens pour pouvoir tourner et faire une autre ligne crénelé, on répetera l'opération 4 fois, ce qui formera un carré

def carre_colore():
  for c in ['red', 'green', 'yellow', 'blue']:
      t.color(c)
      t.forward(75)
      t.left(90)

def motif(n = int(input('Donner un entier : '))): #on demande un entier à l'utilisateur (le fait de le demander dans les paramètres et non dans la fonction évite une répétion de demandes à l'utilisateur si cette fonction est utilisé dans une boucle). On aurait pu faire aussi motif(n) tout simplement.
  if n == 9: #si la longueur est égale à 9, alors on mets de la couleur
    color(couleur()) #c'est juste pour le fun
    forward(n)
    left(60)
    color(couleur())
    forward(n)
    right(120) #car 180 - 60 = 120
    color(couleur())
    forward(n)
    left(60)
    color(couleur())
    forward(n)
  else: #sinon, c'est simplement de couleur noir
    forward(n)
    left(60)
    forward(n)
    right(120) #car 180 - 60 = 120
    forward(n)
    left(60)
    forward(n)


  

def iteration1(): #ce n'est pas la véritable iteration1
  for c in range (3):
    motif()
    right(120)

def iteration2(): #c'est la vraie itération2
  for c in range (6):
    motif()
    left(60)
    motif()
    right(120)

def iteration3aupif(): #il est très joli
  for c in range(6):
      right(120)
      iteration2()
      left(60)
        
def iteration4(): #la véritable itération1 
  for k in range(2):
      motif()
      left(60)
      motif()
      right(120)
  left(120)
    
   
def miniflocon(): #une triplette d'itération qui forme un triangle
  for k in range(3):
    iteration4()
    left(120)

def floconpif(): #un flocon fait a partir du miniflocon
  for c in range (6):
    miniflocon()
    left(60)
    miniflocon()
    right(120)

def flocon(): #le véritable flocon
  for c in range (6):
    iteration4()
    left(60)
    iteration4()
    right(120)
        
def flocooooon() : #faire un flocon avec le flocon
  for k in range(6):
    flocon()
    left(60)
    
def fonction(N):    
  if N==1:
    return 1
  else:
    return fonction(N-1)*N


def delete(): #sert uniquement sur pizo 
  done()




#motif()
#iteration1()
#iteration2()



  
