#CRUZ CANELA EUNICE
Age= []
def main():
    print("¡Hola! Elige una opción:\n\
             1. Crear Protocolo\n\
             2. Mostrar protocolo\n\
             3. Agregar un paso al final de la lista\n\
             4. Añadir un paso en alguna posición indicada\n\
             5. Borrar algún paso\n\
             6. Salir")
while True:
    main()
    opc = int(input( "Elige una opcion para continuar (escribe el número): " ))    
    if opc == 1:
        num = int (input ("Escribe el número de pasos"))
        for _ in range(num):
            paso = input ("Escribe el protocolo: ")
    elif opc==2:
        print ("El protocolo es: "+ str (paso))
    elif opc == 3:
       paso = print("Escribe el nuevo paso: ")
    elif opc ==4:
        paso=print ("Escribe el paso:")
        pos = int (input("Esribe la posición (recuerda que la primera posición es 0): "))
        paso.insert (pos, paso)
        print("Se añadieron los datos en la posición indicada")
    elif opc == 5:
        print(paso)
        bor= int(input ("Escribela posición del dato que deseas borrar(recuerda que la primera posición es 0): "))
        paso.pop(bor)
    elif opc == 8:
        print ("Hasta luego :]")
        break
else:
        print ("Esa opción no es válida")

