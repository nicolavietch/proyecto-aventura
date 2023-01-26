#clase 1 Proyecto: Definiendo la aventura

#Equipamiento - Costo en monedas trekjuls
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego): ")

espada = 200
armadura = 350
pantalones = 250
botas = 150
pan = 20
agua = 5

print("Lista tres objetos del equipamento: Nombre y valor")

print("espada", espada)
print("armadura", armadura)
print("pantalones", pantalones)

#Operadores
print("¿Puedes combinar elementos para prepararte mejor?")

armadura_completa = armadura + pantalones + botas
lonche = agua + pan

print("Armadura completa", armadura_completa)
print("Lonche", lonche)

print("¿El valor de la Armadura completa es menor al del lonche?")

print(armadura_completa < lonche)

print("¿Cuánto valdría comprar unas botas y agua?")

print(botas + agua)

print("¿Si tengo 100 puntos me alcanzará para comprar unas botas?")

print(100 >= botas)
