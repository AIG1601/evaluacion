class persona():
    def registrar(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        while True :
            try:
                 self.edad = int(input("Ingrese su edad: "))
                 break
            except:
                print("Solo puedes ingresar numeros..." + "\n")


class Adultos(persona):
    def registrarAdultos(self):
        self.registrar()
        self.correo = input("Ingrese su correo electrónico: ")
        self.cedula = input("Ingrese su cédula: ")
        
class Niños (persona):
    def registrarNiños(self):
        self.registrar()
        self.jugueteFav = input ("Juguete favorito: ")
        self.colorFav = input ("Color favorito: ")

listaadultos =[]
listaniños=[]
opc = 0


while opc != 3 :
    print("")
    print("-------------MENÚ--------------")
    print("1- Registrar")
    print("2- Mostrar")
    print("3- Salir" + "\n")
    opc = int(input('opcion:'))
    print("")

    if opc == 1:
        opc= 0
        print("¿ Es usted un niños o un adulto ?" +  "\n")
        print("1.niño")
        print("2.adulto")
        print("")
        opc = int(input("Opcion: "))
        print("")
        if opc == 1 :
            niñito = Niños()
            niñito.registrarNiños()
            listaniños.append(niñito)
        elif opc == 2 :
            adultito = Adultos()
            adultito.registrarAdultos()
            listaadultos.append(adultito)

    elif opc == 2 :
        print ("---------- REGISTRADOS ----------")
        for i in listaniños:
            print(i.nombre,i.apellido,i.edad,i.jugueteFav,i.colorFav)
        for i in listaadultos:
            print(i.nombre,i.apellido,i.edad,i.cedula,i.correo)
                
        
            
        

   
    
 
    
