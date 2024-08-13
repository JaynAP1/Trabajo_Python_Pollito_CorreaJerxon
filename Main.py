import json, os

with open("Json/Menu.json", encoding="utf-8") as Menu:
    Menus=json.load(Menu)

with open("Json/Pagos.json", encoding="utf-8") as Pago:
    Pagos=json.load(Pago)

with open("Json/Pedidos.json", encoding="utf-8") as Pedido:
    Pedidos=json.load(Pedido)

Loop=True
while Loop == True:
    os.system("cls")
    print("===============\n1).Hacer pedido.\n2).Pagar pedido.\n3).Modificar Pedido.\n4).Cambiar estado del pedido.\n5).Salir\n===============")
    Opcion1=str(input("Ingrese un numero para moverte por el menu: "))

    if Opcion1 =="1":
        Loop2=True
        while Loop2 == True:
            os.system("cls")
            print("============Pedidos============\n1).Entradas.\n2).Platos fuertes.\n3).Bebidas.\n4).Salir.\n============Pedidos============")
            Opcion1=str(input("Ingrese un numero para moverte por el menu: "))

            if Opcion1=="1":
                os.system("cls")
                print("===========Entradas===========")
                for i in Menus:
                    if i["categoria"]=="entrada":
                        print("Nombre: ",i["nombre"], "Precio: ",i["precio"])
                print("===========Entradas===========")

                input("")
                
            elif Opcion1=="2":
                os.system("cls")
                print("===========Plato Fuerte===========")
                for i in Menus:
                    if i["categoria"]=="plato_fuerte":
                        print("Nombre: ",i["nombre"], "Precio: ",i["precio"])
                print("===========Plato Fuerte===========")

                input("")
            
            elif Opcion1=="3":
                os.system("cls")
                print("===========Bedidas===========")
                for i in Menus:
                    if i["categoria"]=="bebida":
                        print("Nombre: ",i["nombre"], "Precio: ",i["precio"])
                print("===========Bebidas===========")

                input("")
            
            elif Opcion1 =="4":
                print("===============Saliendo===============")
                input("")
                Loop2=False
    
    elif Opcion1=="2":
        print("==============Pagos==============")
        for i in Pedidos:
            if i["pago"]=="no_pagado":
                print("=============================")
                print("Id: ",i["id"],"\nCliente: ",i["cliente"])
                for y in i["items"]:
                    print("Categoria: ",y["categoria"],"\nNombre: ",y["nombre"],"\nPrecio: ",y["precio"])
            
        Comparador=str(input("Ingrese el id del cliente que desea pagar: "))

        for i in Pedidos:
            if Comparador==i["id"]:
                print("Cliente: ",i["cliente"])
                i["pago"]="pagado"
                with open("Json/pedidos.json", "w") as Gpedido:
                    json.dump(Pedidos,Gpedido)

                input("El estado del cliente a cambiado a pagado, presione Enter para continuar.")
            
    elif Opcion1=="3":
        Loop3=True
        while Loop3 == True:
            os.system("cls")
            print("==============Modificiacion==============\n1).Creado a Preparacion.\n2).Preparacion a Servido.\n3).Salir.\n==============Modificiacion==============")
            Opcion1=str(input("Ingrese un numero para moverte por el menu: "))
            
            if Opcion1 == "1":
                os.system("cls")
                for i in Pedidos:
                    if i["estado"]=="creado":
                        print("=============================")
                        print("Id: ",i["id"],"\nCliente: ",i["cliente"])
                        for y in i["items"]:
                            print("Categoria: ",y["categoria"],"\nNombre: ",y["nombre"],"\nPrecio: ",y["precio"])

                Comparador=str(input("Ingrese el id del cliente que desea cambiar a preparacion: "))
                for i in Pedidos:
                    if Comparador==i["id"]:
                        print("Cliente: ",i["cliente"])
                        i["estado"]="preparacion"
                        with open("Json/pedidos.json", "w") as Gpedido:
                            json.dump(Pedidos,Gpedido)

                        input("El estado del cliente a cambiado a preparacion, presione Enter para continuar.")

            elif Opcion1 == "2":
                os.system("cls")
                for i in Pedidos:
                    if i["estado"]=="preparacion":
                        print("=============================")
                        print("Id: ",i["id"],"\nCliente: ",i["cliente"])
                        for y in i["items"]:
                            print("Categoria: ",y["categoria"],"\nNombre: ",y["nombre"],"\nPrecio: ",y["precio"])
                
                Comparador=str(input("Ingrese el id del cliente que desea cambiar a preparacion: "))
                for i in Pedidos:
                    if Comparador==i["id"]:
                        print("Cliente: ",i["cliente"])
                        i["estado"]="servido"
                        with open("Json/pedidos.json", "w") as Gpedido:
                            json.dump(Pedidos,Gpedido)

                        input("El estado del cliente a cambiado a preparacion, presione Enter para continuar.")

            elif Opcion1 == "3":
                os.system("cls")
                print("===============Saliendo===============")
                input("")
                Loop3=False

    elif Opcion1 == "4":
        print("por hacer.")