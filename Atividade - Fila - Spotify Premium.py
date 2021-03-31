class Fila():
    def __init__(self):
        self.S            = []
        self.sentinela    = [None, None] #Inicio, Fim
        self.ED          = {}
        for i in range(len(self.S)):
            self.ED[i] = [False,False]

    def enqueue(self, chave):
        if self.sentinela == [None, None]:
            self.S.append(chave)
            self.ED[0] = [None, 2]
            self.ED[1] = [1, None]
            self.sentinela[0] = 0
            
        else:
            if self.sentinela[1] == None:
                self.S.append(chave)
                self.ED = [0,2]
                self.sentinela[1] = len(self.S)-1
            else:
                self.S.append(chave)
                self.ED[self.sentinela[1]] = len(self.S)-1

    def dequeue(self, i):
        if i == 1:
            if  len(self.S) != 0:
                print(self.S[0])
                del self.S[0]
            else:
                print('...')
        if i == 2:
            if len(self.S) != 0:
                del self.S[0]
            else:
                return
            
                
                




vetor = Fila()
op    = ['\\play', '\\next']

programa = True
while programa:
    try:
        entrada = input()
        if entrada == op[0]:
            vetor.dequeue(1)
        elif entrada == op[1]:
            vetor.dequeue(2)
        elif entrada == 'q':
            programa = False
        else:
            vetor.enqueue(entrada)
            
    except EOFError:
        programa = False


