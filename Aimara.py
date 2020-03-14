class persona():
    def registrar(self):
        self.nombre = input("igrese su nombre")
        self.apellido = input("ingrese su apellido")
        self.edad = input("ingrese su edad")

class adultos (persona):
    def registro(self):
        self.registrar()
        self.cedula = input("ingrese su cedula")
        self.correo = input("ingrese su correo")

class niños (persona):
    def registro(self):
        self.registrar()
        self.color = input("ingrese su color favorito")
        self. juguete = input("ingrese su juguete favorito")

listadultos =[]
listniños=[]
opc = 0


while opc != 3 :
    print("-------------menu-----------")
    print("1-registrar")
    print("2-mostrar")
    print("3-salir")

    opc = int(input('opcion:'))
    if opc == 1:
        print("es usted un niños o un adulto")
        print("1.niño")
        print("2.adulto")
        print("")

        if opc == 1 :
            adultitos = adultos ()
            adultitos.registroad()
            listadultos.append(adultitos)

            niñitos = niños ()
            niñitos. registroni()
            listniños.append(niños)

        if opc == 2 :
            print("n/mostrar")
            for i in listadultos:
                print(i.nombre,i.apellido,i.edad,i.correo,i.cedula)

            for j in listniños:
                print(j.nombre,j.apellido,j.edad,j.juguete,j.color)
        
            
        

   
    
 
    
