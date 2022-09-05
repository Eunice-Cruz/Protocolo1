def main():
    print ("Escribe la opción que deseas realiza\n\
            0.Crear archivo\n\
            1. Escribir protocolo\n\
            2. Agregar paso\n\
            3. Mostrar protocolo\n\
            4. Borrar un paso \n\
            5. Salir")
           
while True:
    main()
    opc = int (input ("Elige una opción para continuar (escribe el número): "))
    if opc==0:
        def crearArchivo():
            archivo = open ("protocolo.txt", "w")
            archivo.close
        crearArchivo()
        print ("Se ha creado el archivo")
    elif opc==1:
        num=int (input ("Escribir numero de pasos: "))
        for _ in range (num):         
            def EscribirArchivo():
                archivo=open("protocolo.txt","a")
                cadena=input("Escribe pasos")
                archivo.write(cadena+"\n")
                archivo.close
            EscribirArchivo()
        print ("Se creó la archivo ")
    elif opc == 2:
        def EscribirArchivo():  
            archivo=open("protocolo.txt","a")
            cadena=input("Escribe el paso que deseas agregar")
            archivo.write(cadena+"\n")
            archivo.close    
        EscribirArchivo()
        print ("Se agregó el paso")
    elif opc==3:
        def LeerArchivo():
            archivo = open ("protocolo.txt", "r")
            linea = archivo.readline()
            while (linea):
                print (linea)
                linea = archivo.readline()
            archivo.close()
        LeerArchivo()
        input ()
    elif opc==4:
        def borrar():                      
            archivo = open ("protocolo.txt", "r")
            linea = archivo.readline()
            while (linea):
                print (linea)
                linea = archivo.readline()
            archivo.close()
            
            archivo = open("protocolo.txt", "w")
            
            pos=int(input ("Numero"))
            linea = 
            pos.remove(linea)
        borrar()
    elif opc == 5:
        print ("Hasta luego :]")
        break
else:
        print ("Esa opción no es válida")

