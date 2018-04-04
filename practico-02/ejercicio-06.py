from datetime import datetime
class Persona:
    def __init__(self, nacimiento):
        self.nacimiento = datetime.strptime(nacimiento, '%d/%m/%Y')

    def edad(self):
        if (datetime.now().month < self.nacimiento.month):
            return (datetime.now().year - self.nacimiento.year - 1)
        elif (datetime.now().month>self.nacimiento.month):
            return datetime.now().year - self.nacimiento.year
        elif (datetime.now().month == self.nacimiento.month):
            if(datetime.now().day >= self.nacimiento.day):
                return datetime.now().year - self.nacimiento.year
            else:
                return datetime.now().year - self.nacimiento.year-1


fecha_str = input("Ingrese fecha de nacimiento [ formato: dd/mm/YYYY ]:\t")
persona = Persona(fecha_str)
print("La edad de la persona es: ", persona.edad(), " años.")
