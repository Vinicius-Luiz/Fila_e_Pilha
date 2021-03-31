### Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)

### Centro de Informática (CIn) (http://www.cin.ufpe.br)

### Graduando em Sistemas de Informação

### IF969 - Algoritmos e Estrutura de Dados

### Autor: Vinícius Luiz da Silva França (vlsf2)

### Email: vlsf2@cin.ufpe.br

### Data: 2020-09-06

### Copyright(c) 2020 Vinícius Luiz da Silva França



#### Explorador de Arquivos - Pilha

> Wilson está aprendendo a navegar na estrutura de arquivos de seu computador utilizando o terminal. Para navegar na estrutura de arquivos são utilizados os seguintes comandos: “pwd” para imprimir o caminho do diretório atual; e “cd” para alterar o diretório atual. Quando "cd" é utilizado com o parâmetro “..”, o diretório atual passa a ser o diretório hierarquicamente superior ao atual, e quando o comando "cd" é utilizado com um parâmetro, o diretório atual passa incluir a pasta que foi passada como parâmetro.

> **Input Specification**
>
> A primeira entrada C é uma string com o caminho atual. O caminho é uma hierarquia de pastas separadas pelo caractere ‘\’. As demais entradas N são comandos M. Os comandos podem receber um parâmetro P separado por espaço do comando na mesma entrada. 	1 < len(C) < 1024 0 < N < ∞        2 < len(M) < 3        1 < len(P) < 1024

> **Output Specification** 
>
> Após o comando “pwd” deve ser impresso o nome do diretório atual

>  **Sample Input #1**

> \wilson\music\nick_minaj  
> pwd  
> cd ..  
> pwd  
> cd nick_minaj  
> cd ..  
> cd ..  
> pwd  

> **Sample Output #1**

>  \wilson\music\nick_minaj  
> \wilson\music  
> \wilson  

> **Sample Input #2**
>
> \  
> cd ..  
> pwd  
> cd wilson  
> pwd  
> cd documents  
> cd cin  
> pwd  

> **Sample Output #2**
>
> \  
> \wilson  
> \wilson\documents\cin  



#### Spotify Premium

> Gabriel assinou o plano premium do Spotify e agora consegue ouvir suas playlists sem interrupções e de maneira não aleatória. As músicas quando adicionadas à playlist são inseridas no final dessa lista. Ao reproduzir uma música (com o comando "\play"), ou quando ela é pulada (com o comando "\next"), ela é eliminada da playlist. As músicas sempre tocam na ordem em que foram inseridas. Quando o comando "next" for executado, a próxima música da playlist é pulada.

> **Input Specification**
>
> As entradas podem ser N linhas M, onde cada uma corresponde ou a um nome de música ou um dos comandos: “\play” (para tocar a primeira faixa da playlist) ou “\next” (para pular para a próxima faixa da playlist).  
>
> 0 < N < ∞  
>
> 0 < len(M) < 100

> **Output Specification**
>
> O comando "\play" executa a primeira faixa da playlist e imprime na tela a música em execução, eliminando a música da playlist. O comando "\next" tira a primeira faixa da playlist e não imprime nada na tela. O reprodutor de áudio só executa a música quando o comando "\play" é executado, ou seja, ele não reproduz automaticamente as músicas. Se o comando "\play" for executado, e não houver nenhuma música na playlist, então deve ser impresso ’...’ (três pontinhos) como saída.

> **Sample Input #1**
>
> The Scientist - Cold Play  
> Geminiano - Djonga  
> Juramento do Dedinho - Mano Walter  
> \play  
> \next  
> \play  
>
> **Sample Output #1**
>
> The Scientist - Cold Play  
> Juramento do Dedinho - Mano Walter

  

> Sample Input #2
>
> \play  
> The Scientist -  Cold Play  
> \play  
> \play  
> Juramento do Dedinho - Mano Walter  
> \play  
> Geminiano - Djonga  
> \next  
> \play    
>
> **Sample Output #2**
>
> ...  
> The Scientist -  Cold Play  
> ...  
> Juramento do Dedinho - Mano Walter  
> ...  

 