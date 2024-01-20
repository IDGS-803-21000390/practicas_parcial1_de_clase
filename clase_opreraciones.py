class Operaciones:
    def __init__(self, lista):
        self.lista = lista
        self.i = 0
        self.j = 0
        self.par = []
        self.inpar = []
       
        
    def par_inpar(self):
        for elemento in self.lista:
            if (elemento / 2) % 1 == 0:
                self.par.append(elemento)
            else:
                self.inpar.append(elemento)
        self.listaSinRepetirPar=set(self.par)
        self.listaSinRepetirInpar=set(self.inpar)
        print("Hay {} numeros pares y son: ".format(len(self.listaSinRepetirPar)))
        for numeroP in self.listaSinRepetirPar:
            print(numeroP)
        print("Hay {} numeros impares y son: ".format(len(self.listaSinRepetirInpar)))
        for numeroI in self.listaSinRepetirInpar:
            print(numeroI)

    def lista_ordenada(self):
        print("Los elementos de la lista en orden son:")
        for elemento in self.lista:
            print(elemento)
    def numeros_repetidos(self):
        self.listaSinRepetir=set(self.lista)
        for elemento in self.listaSinRepetir:
            x=self.lista.count(elemento)
            if x != 1:
                print("CUANTAS VECES SE REPITE {} EN LA LISTA : {}".format(elemento,x))
    
def main(lista):
    obj = Operaciones(lista)
    obj.lista_ordenada()
    obj.par_inpar()
    obj.numeros_repetidos()

if __name__ == "__main__":
    main() 
