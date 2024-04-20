import turtle as t #simplification de turtle.Turtle() pour éviter de le réécrire à chaque fois (cela évite d'écrire turtle.forward(n) par exemple)
#t = turtle.Turtle()

t.speed(0)
def spirale():
  n = 10 #on définit la varriable n à 10
  for c in range (20) : #on fait 10 fois 2 forward n et left 90
    t.forward(n) #on avance de n
    t.left(90) #on tourne à gauche de 90 degrés
    n = n + 10 #on augmente la variable n de 10


def rosace():
  for c in range (36): #j'ai tésté plusieurs fois en modifiant la boucle pour savoir que l'on doit la répéter 36 fois ni plus ni moins.
    t.circle(80) #on fait un cercle
    t.left(10) #on va décaler le cerle en changeant l'orientation

def creneau():
  for g in range (4): #on répète le tout 4 fois pour faire un grand carré
    for d in range (9): #on répète le tout pour faire une grande ligne crénelé
      t.forward(10)
      t.left(90)
      for k in range (2): #simplification pour ne pas écrire forward et right 2 fois
        t.forward(10)
        t.right(90)
      t.forward(10)
      t.left(90)
    t.backward(10)
    t.right(90) #on retourne de 10 en arrière et change de sens pour pouvoir tourner et faire une autre ligne crénelé, on répetera l'opération 4 fois, ce qui formera un carré


def motif(n = int(input('Donner un entier : '))): #on demande un entier à l'utilisateur (le fait de le demander dans les paramètres évite une répétion de demandes à l'utilisateur si cette fonction est utilisé dans une boucle)
  #n = int(input('Donner un entier : ')) #on demande un entier à l'utilisateur
  t.forward(n)
  t.left(60)
  t.forward(n)
  t.right(120) #car 180 - 60 = 120
  t.forward(n)
  t.left(60)
  t.forward(n)


def iteration1():
  for c in range (3):
    motif()
    t.right(120)



def iteration2():
  for c in range (6):
    motif()
    t.left(60)
    motif()
    t.right(120)
  






#motif()
#iteration1()
#iteration2()

###for c in range (3): #on répète 3 fois, car c'est comme un triangle (3 faces)
##  motif()
#  t.right(120) #on tourne pour faire la suite (les autres faces du "triangle")






##########n = 30
#########for c in range (3): #on répète 3 fois, car c'est comme un triangle (3 faces)
########  t.forward(n)
#######  t.left(60)
######  t.forward(n)
#####  t.right(120) #car 180 - 60 = 120
####  t.forward(n)
###  t.left(60)
##  t.forward(n)
 # t.right(120) #on tourne pour faire la suite (les autres faces du "triangle")






















#n = 190
#t.left(90)
#t.forward(200)
#for c in range (20):
  #print(n) #n doit etre superieur à 0, on peut donc utiliser "print" pour le vérifier
#  t.right(90)
#  t.forward(n)
#  n = n - 10





#t.right(90)
#t.forward(90)
#t.right(90)
#t.forward(80)





#for c in ['red', 'green', 'yellow', 'blue']:
    #t.color(c)
    #t.forward(75)
    #t.left(90)

