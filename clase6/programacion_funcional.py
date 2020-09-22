#Caso donde no tenemos entradas
line  = lambda: print ('#'*60)
line()
#vs 
def line_design():
  print ('#'*60)
line_design()

#Caso donde  tenemos una entrada
line  = lambda cantidad: print ('#'*cantidad)
line(2)
def line_design(cantidad):
  print ('#'*cantidad)

line_design(2)

#Caso donde tenemos más de una entrada
sumar = lambda numero1 , numero2 : numero1 + numero2
restar = lambda numero1 , numero2 : numero1 - numero2
multiplicar = lambda numero1 , numero2 : numero1 * numero2
dividir = lambda numero1 , numero2 : numero1 / numero2

print (sumar (35,35))
print (multiplicar (35,35))
print (restar (35,35))
print (dividir (35,35))

#Caso resultados por defecto
sumar = lambda numero1=0 , numero2=0 : numero1 + numero2
print (sumar())
print (sumar(1,2))

#Funciones dentro de otras?
calculadora = lambda accion, valor1=0, valor2=0: print(accion(valor1, valor2))

calculadora(restar,2,2)
calculadora(sumar,2,2)
calculadora(dividir,2,2)
calculadora(multiplicar,2,2)
calculadora(sumar)

# funcion map 
lista = [1,2,3,4]
sumarDos = lambda valor : valor +2
x = list (map (sumarDos, lista))
print(x)

#filter
listaNumeros = [1,2,3,45,23,4,8,9,20]
listaPares = []
for numero in listaNumeros: 
    if numero % 2 == 0 :
        listaPares.append(numero)
print (listaPares)
par = lambda elemento : elemento %2 == 0
pares = list (filter(par,listaNumeros))
print (pares)