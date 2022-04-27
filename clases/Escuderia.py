from xml.dom import NoModificationAllowedErr


class Escuderia():

    def __init__(self):
        self.__nombre = None
        self.__motor = None
        self.__piloto = None
        self.__costoAnual = None
    
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def motor(self):
        return(self.__motor)

    @property
    def piloto(self):
        return(self.__piloto)

    @property
    def costoAnual(self):
        return(self.__costoAnual)

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @motor.setter
    def motor(self,motor):
        if(motor == 'mercedes' or motor == 'ferrari' or motor == 'renault' or motor == 'honda'):
            self.__motor = motor
        else:
            print('Digite una marca de motor valida en minusculas(mercedes/ferrari/renault/honda)')

    @piloto.setter
    def piloto(self,piloto):
        self.__piloto = piloto
    
    @costoAnual.setter
    def costoAnual(self,costoAnual):
        self.__costoAnual = costoAnual