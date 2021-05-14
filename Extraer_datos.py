from Leer_csv import *
from division import *
#from Seleccionar import *

''' Esta clase es para extraer los datos, crear la tabla y llenarla con los datos '''
class Extraer_datos:

    def __init__(self):
        #self.tipo = tipo
        self.contenido = []
        self.dimenciones = []
        self.nueva_lista = []
        self.lista_claves = []
        # la ruta del archivo se debe cambiar con la direccion donde este el csv
        self.archivo = 'C:\\Users\\japb1\\OneDrive - Universidad Autonoma de Yucatan\\facultad\\Análisis exploratorio de datos\\ADA 7\\base de datos\\AGEEML_20212201425282.csv'



    def construir_proceso(self):
        informacion = Leer_csv(self.archivo)
        self.contenido = informacion.contenido
        print("paso 1 completo")
        self.contenido.pop(0)
        for i in self.contenido:
            casteo = division(i)
            casteo.proceso()
            casteo.construir_lista_2()
            self.nueva_lista.append(casteo.nueva_lista)
        #    casteo.calcular_tama()
        #    self.dimenciones.append(casteo.tama)




    def imprimir_resultados(self,clave=2):
        if clave == 0:
            for i in self.contenido:
                print(i)
        elif clave == 1:
            for i in self.dimenciones:
                print(i)
        elif clave == 2:
            for i in self.nueva_lista:
                print(i)
        else:
            print("no valido")




    def imprimir_resultados_2(self):
        for i in self.contenido:
            print(i)








'''  proceso de extraccion de los datos,basta con hacer correr esta 
clase para extraer los datos del csv y ponerlos en una tabla '''
Extraer= Extraer_datos()
Extraer.construir_proceso()
Extraer.imprimir_resultados(2)

