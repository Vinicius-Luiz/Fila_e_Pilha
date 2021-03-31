def main():
    class Pilha():
        def __init__ (self):
            self.S = []
            self.topo = 0            
        def imprimevetor (self, string = '\\'):
            for i in self.S:
                string += i
                string += '\\'
            if len(string) != 1:
                string = string[:-1]
            else:
                string = '\\'
            print(string)
            
        def setTopo(self, operacao):
            self.topo += operacao
            return self.topo

        def getTopo (self):
            return self.topo

        def stack_empty (self):
            if len(self.S) == 0:
                return True
            else:
                return False

        def push (self, chave):
            topo = self.setTopo(1)    
            self.S[topo] = chave            

        def pop(self):
            if self.stack_empty():
                return
            else:
                self.S.pop()
                topo = self.setTopo(-1)

    def manipular_entrada(entrada):
        b  = '\\'
        b += entrada
        b  = b.split('\\')
        for i in b:
            word = ''
            for c in i:
                if c == '\n':
                    vetor.S.append(word)
                    c = 'n'
                    word  = ''
                    word += c
                else:
                    word += c
            if word != '':
                vetor.S.append(word)

    def manipular_cd(entrada, s = ''):
        for c in entrada:
            s += c
            if s == 'cd ':
                s = ''
        return s

    vetor    = Pilha()
    op       = ['pwd','cd ..', 'cd ']
    programa = True
    while programa:
        try: 
            entrada = input()
            if entrada == op[0]:
                vetor.imprimevetor()
                
            elif entrada == op[1]:
                vetor.pop()
                
            elif op[2] in  entrada:
                string = manipular_cd(entrada)
                manipular_entrada(string)
                
            elif entrada not in op:
                manipular_entrada(entrada)
        except EOFError:
            programa = False


if __name__ == '__main__':
    main()

