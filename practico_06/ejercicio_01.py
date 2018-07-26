import sys
sys.path += ['/home/favio/Github/soporte/']
# print(sys.path)

from practico_05.base import Socio
from practico_05.ejercicio_02 import DatosSocio

class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            socio= self.datos.buscar(id_socio)
            return(socio)
        except Exception as e:
            return None


    def buscar_dni(self, dni_socio):
        try:
            socio=self.datos.buscarDni(dni_socio)
            return socio
        except Exception as e:
            return None

        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """


    def todos(self):

        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios=self.datos.todos()
        return socios


    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        val1=self.regla_1(socio)
        val2=self.regla_2(socio)
        val3=self.regla_3()
        if (val1 & val2 & val3):
            validacion=self.datos.alta(socio)
            if (validacion==False):
                return False
            else:
                return True
        else:
            return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            validacion=self.datos.baja(id_socio)
            return validacion
        except Exception as e:
            return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            validacion=self.datos.modificacion(socio)
            if (validacion==False):
                return False
            else:
                return True
        except Exception as e:
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        socios=self.todos()
        for i in socios:
            if(i.dni==socio.dni):
                return False
            else:
                return True


    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre)>self.MIN_CARACTERES & len(socio.nombre)<self.MAX_CARACTERES):
            if (len(socio.apellido)>self.MIN_CARACTERES & len(socio.apellido)<self.MAX_CARACTERES):
                return True
        else:
            return False


    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        socios=self.todos()
        if (len(socios)<self.MAX_SOCIOS):
            return True
        else:
            return False
