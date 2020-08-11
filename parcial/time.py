import casos
import time

n=0
inicio = time.time() 
casos.caso1(n)
tiempo_caso1 = time.time()- inicio
print(tiempo_caso1)
inicio = time.time() 
casos.caso2(n)
tiempo_caso2 = time.time()- inicio
print(tiempo_caso2)

if tiempo_caso1>tiempo_caso2:
  print("Es mejor el caso 2")
else: 
  print("Es mejor el caso 1")

