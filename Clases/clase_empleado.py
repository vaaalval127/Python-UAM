from salario_neto import salario_neto
 
class Empleado:
    def __init__(self, nombre, salarioBruto):
        self.__nombre = nombre
        self.__salarioBruto = salarioBruto

    def get_nombre(self):
        return self.__nombre

    def get_salarioNeto(self):
        return salario_neto(self.__salarioBruto)
    