
''' Cambiar  nombre a Castear'''
class division:

    ''' Se para al costructor al inviduo y se hace el cssteo de los datos'''
    def __init__(self,cadena):
        self.cadena = cadena.pop()
        self.lista_cadena = []
        self.nueva_lista = []
        self.tama = None


    def proceso(self):
        self.lista_cadena = self.cadena.split()
        #print(self.lista_cadena)

    def calcular_tama(self):
        self.tama = len(self.lista_cadena)

    def construir_lista(self):
        self.calcular_tama()
        for i in range(self.tama):
            self.nueva_lista.append(self.lista_cadena[i])


    def construir_lista_2(self):
        #print("prueba")
        #self.nueva_lista.append(float(self.lista_cadena[-4]))
        self.nueva_lista.append(float(self.lista_cadena[-7]))
        self.nueva_lista.append(float(self.lista_cadena[-8]))
        #poner una expecion para el caso de la poscion -4
        try:
            self.nueva_lista.append(float(self.lista_cadena[-4]))
        except ValueError:
            self.nueva_lista.append(0)







    def hacer_ajuste_3(self):
        self.nueva_lista.append(int(self.lista_cadena[4]))
        for i in range(20,30):
            self.nueva_lista.append(int(self.lista_cadena[i]))
            #print(i)
        self.lista_cadena = self.nueva_lista



    # Metodo para pruebas locales, NO USAR en el programa global
    def imprimir_cadena(self):
        print(self.lista_cadena)
        print(len(self.lista_cadena))
        #print(self.nueva_lista)
        #for i in self.lista_cadena:
        #    print(i)

        #print(float(self.lista_cadena[2]))


##pruebas del nuevo metodo
#lista_a = ['2021-03-23\tc1baa1\t1\t12\t20\t2\t20\t20\t067\t2\t2021-01-19\t2021-01-15\t9999-99-99\t2\t1\t38\t1\t97\t2\t2\t1\t2\t2\t2\t1\t2\t2\t1\t2\t2\t2\t1\t4\t2\t97\t5\t99\tMÃ©xico\t97\t2']

#prueba2 = division(lista_a)
#prueba2.proceso()
#prueba2.hacer_ajuste_3()
#prueba2.imprimir_cadena()