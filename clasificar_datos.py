class clasificar_datos:


    def __init__(self,lista_listas,valor = 10000):
        self.valor_clasificacion= valor
        self.lista_listas = lista_listas
        self.lista_menores = []
        self.lista_mayores = []



    def hacer_clasificacion(self):
        for i in self.lista_listas:
            if i[2] > self.valor_clasificacion:
                self.lista_mayores.append(i)
            else:
                self.lista_menores.append(i)


    def imprimir_resultados(self):
        print("lista mayores:")
        for i in self.lista_mayores:
            print(i)
        print("lista menores:")
        for i in self.lista_menores:
            print(i)


#print("prueba")
listaA = [ [-102.382739, 21.865298, 7.0],
[-102.166586, 21.766347, 3.0],
[-102.371736, 21.664743, 0.0],
[-102.245433, 21.840385, 11.0],
[-102.166451, 21.782366, 354.0],
[-102.136513, 21.76609, 144.0],
[-102.35464, 21.888178, 7.0],
[-102.346432, 21.899666, 0.0],
[-102.353023, 21.878049, 0.0],
[-102.329403, 21.832967, 37.0],
[-102.242425, 21.856659, 27.0],
[-102.106057, 21.770209, 2.0],
[-102.374793, 21.822133, 9.0],
[-102.358812, 21.90731, 575.0],
[-102.451476, 21.685867, 14.0],
[-102.212601, 21.907652, 7.0],
[-102.346626, 21.892211, 6.0]
]

prueba1= clasificar_datos(listaA,250)
prueba1.hacer_clasificacion()
prueba1.imprimir_resultados()

