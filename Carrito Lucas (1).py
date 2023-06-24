#carrito de compras

import os


opcion = ""
DicProductos = {
    "01" : {
        "Codigo" : 100,
        "Nombre" : "Mate",
        "Marca": "Pampa",
        "Precio": 6500,
        "Stock": 5,
        "Material": "pvc" },

    "02" : {
        "Codigo" : 200,
        "Nombre" : "Mate",
        "Marca": "Lalo",
        "Precio": 3500,
        "Stock": 6,
        "Material": "pvc y goma" },
     "03" : {
        "Codigo" : 300,
        "Nombre" : "TermoBarato",
        "Marca": "Romania",
        "Precio": 11500,
        "Stock": 5,
        "Material": "Acero" },
     "04" : {
        "Codigo" : 400,
        "Nombre" : "TermoCaro",
        "Marca": "Stanley",
        "Precio": 21000,
        "Stock": 3,
        "Material": "acero" } }
primer_producto = DicProductos ["01"]
segundo_producto = DicProductos ["02"]
tercero_producto = DicProductos ["03"]
cuarto_producto = DicProductos ["04"]

DicCarrito = {}

 #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#

    
def verCarrito(carrito,DicProductos):
    regresarLista = [DicProductos,carrito]
    if len(carrito) == 0:
        print("El carrito se encuentra vacio ")
    else:
        print ("Los productos en el carrito son los siguientes: ")
        print (DicCarrito)
        print("Desea modificar el carrito? \n1----> Si \n2---->No   ")
        opcion = input("")
        if opcion == "1":
            codigo = input ("Ingrese el codigo del producto a eliminar \n")
            bandera = False

            if codigo in carrito:
                print("Producto encontrado ")
                bandera = True

            if bandera == False:
                print("Producto no encontrado, Intente nuevamente")
            else:
                numero = int(input ("Cuantos productos desea eliminar? \n"))
                if numero >= 0 and numero <= carrito[codigo]["Cantidad"]:
                    
                    if numero == carrito[codigo]["Cantidad"]:
                        carrito.pop(codigo)
                    else:
                        nuevoNumero = carrito[codigo]["Cantidad"] - numero

                        carrito[codigo]["Cantidad"] = nuevoNumero
                        carrito[codigo]["Subtotal"] = nuevoNumero * carrito[codigo]["Precio"]
                    for cod in DicProductos:
                        if int(codigo) == DicProductos[cod]["Codigo"]:
                            reponer = DicProductos[cod]["Stock"]
                            DicProductos[cod]["Stock"] = (reponer + numero)
                    regresarLista = [DicProductos,carrito]

                else:
                    print("Su carrito no posee esa cantidad...")
                
    return regresarLista

                    


        
 #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#

def mostrarProductosCompletos():    
    for codigo, producto in DicProductos.items():
        print("Codigo: ", producto["Codigo"])
        print("_______________________")
        print("Nombre: ", producto["Nombre"])
        print("_______________________")
        print("Marca: ", producto["Marca"])
        print("_______________________")
        print("Precio: ", producto["Precio"])
        print("_______________________")
        print("Stock: ", producto["Stock"])
        print("_______________________")
        print("Material: ", producto["Material"])
        print("  ")
        print("  ")

 #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#

def mostrarProductosBreve():
    cod = input("Por favor ingrese el codigo o nombre del producto...")
    bandera = False
    for Codigo , Nombre in DicProductos.items():
        if (str(DicProductos[Codigo]["Codigo"]) == cod) or (DicProductos[Codigo]["Nombre"] == cod):
            print("Producto encontrado")
            print("Codigo: ", DicProductos[Codigo]["Codigo"])
            print("_______________________")
            print("Nombre: ", DicProductos[Codigo]["Nombre"])
            print("_______________________")
            print("Precio: ", DicProductos[Codigo]["Precio"])
            print("_______________________")
            print("Stock: ", DicProductos[Codigo]["Stock"])
            print("  ")
            print("  ")

            bandera = True
    if bandera == False:
            print("Producto no encontrado, Intente nuevamente")

  #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#
      

def buscarProductos(DicProductos, carrito):
    regresarLista = [DicProductos,carrito]
    cod = input("Ingrese el codigo o nombre del producto...")
    bandera = False
    for key , Nombre in DicProductos.items():
        if (str(DicProductos[key]["Codigo"]) == cod) or (DicProductos[key]["Nombre"] == cod): ## if cod in DicPorductos[key]
            llave = key
            print("Producto encontrado")
            print(" ")
            print("Codigo: ", DicProductos[key]["Codigo"])
            print("_______________________")
            print("Nombre: ", DicProductos[key]["Nombre"])
            print("_______________________")
            print("Marca: ", DicProductos[key]["Marca"])
            print("_______________________")
            print("Precio: ", DicProductos[key]["Precio"])
            print("_______________________")
            print("Stock: ", DicProductos[key]["Stock"])
            print("_______________________")
            print("Material: ", DicProductos[key]["Material"])
            print("  ")
            print("  ")
            bandera = True
    if bandera == False:
        print("Producto no encontrado, Intente nuevamente")
    else:
        banderaDos = True
        while banderaDos == True:
            print("Desea agregarlo al carrito? \n1----> Si \n2----> No ")
            verificacion = input("")
            if verificacion == "1":
                banderaTres = True
                while banderaTres:
                    print("Cuantos productos desea agregar a su carrito? ")
                    numero =input("")

                    if numero.isnumeric() == False:
                        print("Valor invalido, ingrese un numero...")
                    else:
                        numero = int(numero)

                        if (numero > DicProductos[llave]["Stock"]) and (numero > 0):
                            print("Stock insuficiente ")
                        else:
                            if llave in carrito:
                                nuevoNum = carrito[llave]["Cantidad"] + numero
                            else:
                                nuevoNum = numero
                            subtotal = (DicProductos[llave]["Precio"] * nuevoNum)
                            codigo = str(DicProductos[llave]["Codigo"])
                            DicCarrito[codigo] = {"Nombre" : DicProductos[llave]["Nombre"] , "codigo" : codigo , "Cantidad" : nuevoNum , "Precio" : DicProductos[llave]["Precio"], "Subtotal" : subtotal}
                            regresarLista[1] = DicCarrito

                            newStock = DicProductos[llave]["Stock"] - numero
                            DicProductos[llave]["Stock"] = newStock

                            regresarLista[0] = DicProductos

                            
                            banderaTres = False
                            banderaDos = False
            elif verificacion == "2":
                banderaDos = False
            else:
                print("Opcion no valida. Responda si o no")
    return regresarLista
           

#•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#


def finalizarCompra(DicCarrito, DicProductos):
    banderaX = False 
    
    while banderaX == False:

        total = 0
        for llave in DicCarrito:
            print("Usted esta por adquirir:")
            print("Nombre: ", DicCarrito[llave]["Nombre"])
            print("Marca: ", DicCarrito[llave]["Marca"])
            print("Cantidad: ", DicCarrito[llave]["Stock"])
            print("")
            print("")
            print("")
            subtotal = DicCarrito[llave]["Cantidad"] * DicProductos[llave]["Precio"]

            print("el subtotal de su compra es de: ")
            print ("$" + str(subtotal))
        
            total += subtotal
        opcion = input("Esta conforme con su compra? 1) SI\n2) NO\n")

        if (opcion == "SI") or (opcion == "1") or (opcion == "si"):
            print ("El total de su compra es de: " + "$" + total)
            print("Gracias por visitar Artesanias Lucas, vuelva pronto!!")
            salir == False
            DicCarrito.clear()
        elif (opcion == "NO") or (opcion == "2") or (opcion == "no"):
            banderaX = True
        
#Falta completar


#•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦


salir = True
spacio = ""

while salir == True:
    print("Bienvenidos a Artesanias Lucas!! \n A continuacion nuestro menu: \n 1-Mostrar productos. \n 2-Detalles del producto. \n 3-Ver carrito. \n 4-Realizar compra. \n 5-Finalizar compra. \n 6-Salir.")
    opcion = input("Que desea realizar? ")
    if opcion == "1":
        mostrarProductosCompletos()
        espacio = input("Presione una tecla para continuar.....")
        os.system("cls")
    elif opcion == "2":
        mostrarProductosBreve()
        espacio = input("Presione una tecla para continuar.....")
        os.system("cls")
    elif opcion == "3":
        modificarCarrito = verCarrito(DicCarrito,DicProductos)
        DicProductos = modificarCarrito[0]
        DicCarrito = modificarCarrito[1]
        espacio = input("Presione una tecla para continuar.....")
        os.system("cls")
    elif opcion == "4":
        dobleDic = buscarProductos(DicProductos, DicCarrito)
        DicCarrito = dobleDic[1]
        DicProductos = dobleDic[0]
        espacio = input("Presione una tecla para continuar.....")
        os.system("cls")
    elif opcion == 5:
        finalizarCompra(DicProductos, DicCarrito)
    elif opcion == 6:
        print("Gracias por visitar Artesanias Lucas, vuelva pronto!!")
        salir == False



 #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#
 #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#
 #•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦#
   






"""def validarOpciones():
    if opcion == 1:
            mostrarProductosCompletos()           
   
    if opcion == 2:
            #mostrarProductoBreve()

    if opcion == 3:
            #buscarProductoPorCodigo()  
"""







"""#while salir :
    #opcion = int(input("Que desea realizar? "))
    #validarOpciones (1 al 5)
   #aca hacer una funcion para validar opcion , si existe la opcion
   #derivar a la opcion correspondiente a su ves con otra funcion
   #validarOpciones"""


   