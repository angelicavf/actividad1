from tabulate import tabulate
import numpy as np

lista_producto = [[1, "candado", 4000], [2, "tornillo", 1500], [
    3, "martillo", 6000], [4, "huincha", 2500], [5, "alicate", 6000]]

comunas = [[1, "estacion Central", 2000], [2, "Providencia", 2500],
           [3, "Las condes", 3000], [4, "Quinta Normal", 2000]]

totalFinal = 0
subtotal = 0
cantidad = 0
fin = 1
despacho = 0
tenviocompra = 0
aux = ""
factura = []

# mostrando la lista de productos

print("Bienvenido a Ferreteria AYV, a continuacion se despliega la lista de productos disponibles: ")

print(tabulate(lista_producto, headers=["id", "Producto", "Precio"]))

# selaccionando la opcion del usuario

while fin == 1:
    opcion = 100
    while opcion > len(lista_producto):
        opcion = int(input("ingrese el id de producto a comprar: "))
        if opcion > len(lista_producto):
            print("¡Id no válido!")

    aux = lista_producto[opcion-1][1]
    cantidad = int(
        input("ingrese la cantidad de productos que desea comprar de {}: ".format(aux)))


# calculando el valo de un porduto seleccionado, con la cantidad indicada

    subtotal = lista_producto[opcion-1][2] * cantidad
    nombre = str(lista_producto[opcion-1][1])
    print("El subtotal a pagar por ", cantidad,
          " ", nombre, " es: ", subtotal)

    totalFinal = subtotal+totalFinal
    fin = int(
        input("si desea finalizar la compra ingrese 0 o 1 para continuar comprando :"))

    factura.append([aux, subtotal])


factura.append(['Total Compra', totalFinal])
print("El total de su compra es: ", totalFinal)


# selecciona si quiere despacho

fin = int(input(
    "Si desea contratar despacho ingrese 1 en caso contrario 0 para finalizar compra: "))

if(fin == 1):

    print(tabulate(comunas, headers=["id", "comuna", "Envio"]))

    opcion = 100

    while opcion > len(comunas)+1:
        opcion = int(input("Indique el numero de su comuna: "))
        if opcion > len(comunas):
            print("¡Comuna no valida!")

    tenviocompra = comunas[opcion-1][2] + totalFinal
    aux = str(comunas[opcion-1][1])

    print("El total de su compra con envio es: ", tenviocompra,
          " con despacho a la comuna de ", aux)
    factura.append(['Total Compra + envío', tenviocompra])
    print(tabulate(factura, headers=["Detalle", "Monto"]))

else:
    print("El total de su compra sin despacho es: ", totalFinal)
