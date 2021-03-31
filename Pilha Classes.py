import numpy as np
class Pilha():
    def __init__ (self):
        '''Construtor'''
        self.S = np.full(100, None) #Tamanho do vetor
        self.topo = 0
        
    def imprimevetor (self, cont = 0):
        '''Imprime Vetor'''
        for i in self.S:
            if cont == 0:
                cont += 1
                pass
            elif i != None:
                print(i)
        print('\n') 

    def setTopo(self, operacao):
        '''Altera valor atual do Topo'''
        self.topo += operacao
        return self.topo

    def getTopo (self):
        '''Imprime valor atual do Topo'''
        return self.topo

    def stack_empty (self):
        '''Verifica se Vetor está vazio'''
        if self.topo == 0:
            return True
        else:
            return False

    def push (self, chave):
        '''Insere novo elemento'''
        ##Elementos começarão a ser inseridos no índice 1 do vetor, e não no índice 0 (achei menos trabalhoso)
        topo = self.setTopo(1)    
        self.S[topo] = chave
        

    def pop(self):
        '''Remove elemento'''
        if self.stack_empty():
            return
        else:
            #clean = self.S[self.topo] ##Caso eu queira retornar o removido
            self.S[self.topo] = None
            topo = self.setTopo(-1)
            #return clean ##Caso eu queira retornar o removido
    

## [...]
##[30, 2, 4, 5]
##[30, 2, 4, 5, 62]
##[30, 2, 4, 5, 62, 12]
##[30, 2, 4, 5, 62]
##[30, 2, 4, 5]
##[30, 2, 4]

vetor    = Pilha()
vetor.push(30)
vetor.imprimevetor()

vetor.push(2)
vetor.imprimevetor()

vetor.push(4)
vetor.imprimevetor()

vetor.push(5)
vetor.imprimevetor()

vetor.push(62)
vetor.imprimevetor()

vetor.push(12)
vetor.imprimevetor()

vetor.pop()
vetor.imprimevetor()

vetor.pop()
vetor.imprimevetor()

vetor.pop()
vetor.imprimevetor()




