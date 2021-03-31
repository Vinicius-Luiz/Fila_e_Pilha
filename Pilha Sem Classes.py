import numpy as np
def imprimevetor (S, cont = 0):
    '''Imprirme Vetor'''
    for i in S:
        if cont == 0:
            cont += 1
            pass
        elif i != None:
            print(i)
    print('\n')

def setTopo(S, operacao):
    '''Modifica valor do Topo'''
    S[0] += operacao
    return S[0]

def getTopo (S):
    '''Imprime valor do Topo'''
    return S[0]

def stack_empty (S):
    '''Verifica se Vetor está vazio'''
    if S[0] == 0:
        return True
    else:
        return False

def push (S, chave):
    '''Insere novo Elemento'''
    topo = setTopo(S, 1)    
    S[topo] = chave
    

def pop(S):
    '''Remove Elememnto'''
    if stack_empty(S):
        return
    else:
        #clean = S[int(S[0])] ##Caso eu queira retornar o removido
        S[int(S[0])] = None
        topo = setTopo(S, -1)
        #return clean ##Caso eu queira retornar o removido
    

## [...]
##[30, 2, 4, 5]
##[30, 2, 4, 5, 62]
##[30, 2, 4, 5, 62, 12]
##[30, 2, 4, 5, 62]
##[30, 2, 4, 5]
##[30, 2, 4]

vetor    = np.full(1000, None) 
vetor[0] = 0 #topo
no       = push(vetor, 30), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = push(vetor, 2), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = push(vetor, 4), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = push(vetor, 5), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = push(vetor, 62), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = push(vetor, 12), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = pop(vetor), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = pop(vetor), print('topo:', getTopo(vetor))
imprimevetor(vetor)
no       = pop(vetor), print('topo:', getTopo(vetor))
imprimevetor(vetor)



