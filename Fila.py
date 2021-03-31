class Fila():
    def __init__(self):
        self.sentinela   = [None, None]
        self.listaLigada = {} 

    def enqueue (self, chave):
        if self.getInicio() == None and self.getFim() == None:
            self.listaLigada[0] = [chave ,0, None]
            self.sentinela[0] = 0

        elif self.getInicio() != None and self.getFim() == None:    
            self.listaLigada[1] = [chave, self.getInicio(), 1]
            self.sentinela[1]   = 1
        else:
            self.listaLigada[self.getFim()+1] = [chave, self.getInicio(), self.getFim()+1]
            self.sentinela[1] += 1

    def dequeue(self):
        self.listaLigada[self.getInicio()] = [None, False, False]
        self.sentinela[0] += 1
        self.apagaListaVazia()

    def getInicio(self):
        return self.sentinela[0]

    def getFim(self):
        return self.sentinela[1]

    def imprime(self):
        lista = []
        for i in self.listaLigada:
            if self.listaLigada[i][0] == None:
                pass
            elif self.listaLigada[i][0] is not type(None):
                lista.append(self.listaLigada[i][0])
        return lista

    def apagaListaVazia (self):
        lista = []
        for i in self.listaLigada:
            if self.listaLigada[i][0] == None:
                pass
            elif self.listaLigada[i][0] is not type(None):
                lista.append(self.listaLigada[i][0])
                break
        if len(lista) == 0:
            self.sentinela   = [None, None]
            self.listaLigada = {}


f = Fila()
