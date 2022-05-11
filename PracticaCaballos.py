import random
import cv2

a = [0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0]
e = [0, 0, 0, 0, 0]

infitte = [a, b, c, d, e, 1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,]

stop = False
counter = 0
todos = []
top5 = []
primero = []
segundo = []

def race(list):
  global stop 
  i = 0
  if counter < 5:
    while i < 5:
      list[i] = random.uniform(1, 20).__round__(1) #km /hr
      todos.append(list[i])
      i += 1

    list.sort()

  if counter == 5:
    i = -5
    todos.sort()
    print('\ntodos: ', todos)
    while i < 0:
      top5.append(todos[i])
      i += 1
    print('\ntop5: ', top5)

    primero = top5[-1]
    print('\nPrimer Lugar: ', primero)

  if counter == 6:
    todos.pop(-1)
    segundo = todos[-1]
    print('\nSegundo: ', segundo)
    stop = not stop

  return 1

 
while(stop == False):
  counter += race(infitte)

print('\nSe nececistan minimo: ', counter, 'carreras')


def printGrafo(caballos):
  #Initialice 
  grafo = 255*np.ones((250,550,3),dtype=np.uint8)
  font = cv2.FONT_HERSHEY_TRIPLEX

  # Creación de los nodos del grafo
  #Primer lugar
  cv2.circle(grafo,(250,50),10,(0,0,0),-1)
  cv2.putText(grafo,'1er: ' + str(VelCaballos[4,4]),(280,50),font,1,(0,0,0),2,cv2.LINE_AA)

  #Segundo lugar
  cv2.circle(grafo,(250,100),10,(0,0,0),-1)
  cv2.putText(grafo,'2do: ' + str(VelCaballos[3,4]),(280,100),font,1,(0,0,0),2,cv2.LINE_AA)
  cv2.line(grafo,(250,100),(250,50),(255,0,0),2)

  #Lugares extra 
  cv2.circle(grafo,(125,150),10,(0,0,0),-1)
  cv2.putText(grafo,'3er',(150,150),font,1,(0,0,0),2,cv2.LINE_AA)
  cv2.line(grafo,(125,150),(250,150),(255,0,0),2)

  cv2.circle(grafo,(375,150),10,(0,0,0),-1)
  cv2.putText(grafo,'4to',(395,150),font,1,(0,0,0),2,cv2.LINE_AA)
  cv2.line(grafo,(375,150),(250,150),(255,0,0),2)

  cv2.circle(grafo,(125,200),10,(0,0,0),-1)
  cv2.putText(grafo,'5to',(150,200),font,1,(0,0,0),2,cv2.LINE_AA)
  cv2.line(grafo,(125,200),(250,200),(255,0,0),2)

  cv2.circle(grafo,(375,200),10,(0,0,0),-1)
  cv2.putText(grafo,'6to',(395,200),font,1,(0,0,0),2,cv2.LINE_AA)
  cv2.line(grafo,(375,200),(250,200),(255,0,0),2)

  #Conexiones extras
  cv2.line(grafo,(250,150),(250,100),(255,0,0),2)
  cv2.line(grafo,(250,200),(250,150),(255,0,0),2)

  #Impresión del grafo
  cv2.imshow('Grafo',grafo)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
