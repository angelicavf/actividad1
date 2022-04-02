
lista_producto = [[1, "candado", 4000], [2, "tornillo", 1500], [
    3, "martillo", 6000], [4, "huincha", 2500], [5, "alicate", 6000]]

comunas = [[1, "estacion Central", 2000], [2, "Providencia", 2500],
           [3, "Las condes", 3000], [4, "Quinta Normal", 2000]]

totalFinal = 0
subtotal = 0
opcion = 0
cantidad = 0
fin = 1
despacho = 0
tenviocompra = 0
nombrecomuna = ""
opcion_comuna = 0
z = 0

# mostrando la lista de productos

print("{:<8} {:<15} {:<10}".format('id', 'producto', 'precio'))

for v in lista_producto:
    id, producto, precio = v
    print("{:<8} {:<15} {:<10}".format(id, producto, precio))


# selaccionando la opcion del usuario

while fin == 1:

    opcion = int(input("ingrese el id de producto a comprar: "))
    cantidad = int(
        input("ingrese la cantidad de productos que desea comprar: "))

# calculando el valo de un porduto seleccionado, con la cantidad indicada

    for x in range(len(lista_producto)-1):
        if lista_producto[x][0] == opcion:
            subtotal = lista_producto[x][2] * cantidad
            nombre = str(lista_producto[x][1])
            print("El subtotal a pagar por ", cantidad,
                  " ", nombre, " es: ", subtotal)

    totalFinal = subtotal+totalFinal
    fin = int(
        input("si desea finalizar la compra ingrese 0 o 1 para continuar comprando :"))

print("El total de su compra es: ", totalFinal)

# selecciona si quiere despacho

despacho = int(input(
    "si desea contratar despacho ingrese 1 en caso contrario 0 para finalizar: "))

if(despacho == 1):

    print("{:<5} {:<20} {:<10}".format('id', 'Comuna', 'envio'))

    for v in comunas:
        id, comuna, envio = v
        print("{:<5} {:<20} {:<10}".format(id, comuna, envio))

    opcion_comuna = int(input("Indique el numero de su comuna: "))

    for z in range(len(comunas)-1):
        if comunas[z][0] == opcion_comuna:
            tenviocompra = comunas[z][2] + totalFinal
            nombrecomuna = str(comunas[z][1])

    print("El total de su compra con envio es: ", tenviocompra,
          " con despacho a la comuna de ", nombrecomuna)
else:
    print("El total de su compra sin despacho es: ", totalFinal)
