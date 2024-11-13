import math

print ("VOLUMEN DEL CILINDRO DISPENSADOR ")

class Automatiza_comida:
    def __init__(self, status):
        self.status = " "
    
    def verde(self, sensor =16964.6):
        print ("El dispensador esta en el 80% - CODIGO VERDE")
        
    def Azul(self):
        print ("El dispensador esta en el 60% - CODIGO AZUL")

    def Naranja(self):
        print ("El dispensador esta en el 40% - CODIGO NARANJA")
        print ("MENSAJE ALERTA" )

    def Amarillo(self):
        print ("El dispensador esta en el 20% - CODIGO AMARILLO")
        print ("SEGUNDO MENSAJE ALERTA" )
    
    def Negro(self):
        print ("El dispensador esta en el 0% - CODIGO NEGRO")
        print ("PRENDER ALARMA" )


    def Volumen(self, radio, altura, sensor):
        Volumen_cilindro = math.pi * radio**2 * altura 
        print ("El volumen del cilindro es: ", Volumen_cilindro)
        volumen_ochenta = Volumen_cilindro* 80/100
        # 16964.600329384884
        volumen_sesenta = Volumen_cilindro* 60/100
        # 12723.450247038663
        volumen_cuarenta = Volumen_cilindro* 40/100
        # 8482.300164692442
        volumen_veinte = Volumen_cilindro* 20/100
        # 4241.150082346221
       
        if sensor >= 16964.6:
            Automatiza_comida.verde(self)
        elif sensor >= 12723.4: 
            Automatiza_comida.Azul(self)
        elif sensor >= 8482.3:
            Automatiza_comida.Naranja(self)
        elif sensor >= 4241.1:
            Automatiza_comida.Amarillo(self)
        else:
            Automatiza_comida.Negro(self)
       
Automatiza = Automatiza_comida("uno")
Automatiza.Volumen(15,30, 16964.6)