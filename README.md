# Introducao_a_comp_python
EP1: Neste EP a sua tarefa será verificar se um número pode ser escrito como a soma de quadrados de quatro números primos consecutivos ou não. O programa terá dois modos de operação. No primeiro modo o programa receberá do usuário cinco números naturais n1, n2, n3, n4 e n e retornará a informação de se n pode ou não ser escrito como a soma dos quadrados de n1, n2, n3 e n4. No segundo modo o programa receberá do usuário um único número natural n e retornará os quatro primos consecutivos cuja soma dos quadrados seja igual a n ou a informação de que não é possível representar n como a soma dos quadrados de quatro primos consecutivos.

Seu programa deve ler do teclado o modo de operação, que será 1 ou 2. Caso o usuário digite 1, o programa deverá funcionar no primeiro modo de operação e nesse caso deverá ler do teclado os cinco números naturais n1, n2, n3, n4 e n e imprimir verdadeiro caso n seja igual à soma dos quadrados de n1, n2, n3, n4 ou falso caso contrário.

Caso o usuário digite 2 como sendo o modo de operação, seu programa deve funcionar no segundo modo de operação e nesse caso ele deve imprimir os quatro números primos consecutivos cuja soma dos quadrados seja igual ao número passado como entrada ou a mensagem falso caso isso não seja possível.


EP2: 1.Escreva uma função polinomioComRaiz que recebe dois parâmetros p e b e devolve True caso o real b seja raiz do polinômio representado pela lista p, ou False caso contrário. 
2.Escreva uma função polinomioQuociente que recebe dois parâmetros p e b e devolve a lista que representa o polinômio quociente 
 
 onde 
 b é uma raiz do polinômio 
 representado por p. Suponha que 
 tem grau ao menos 
 (não é necessário verificá-lo).
3.Escreva uma função listaCanonicaDeRaizes que recebe um parâmetro p com a lista que representa o polinômio 
 e devolve a lista canônica das raízes inteiras


EP3:
este exercício-programa, você terá que desenvolver várias funções relacionadas com um modelo de simulação de contaminação por vírus. A função main() já está sendo fornecida pronta. Também são fornecidos os protótipos/cabeçalhos das funções a serem desenvolvidas. Não apague ou altere a função main(). Não altere os protótipos/cabeçalhos das funções (isto é, nome das funções e sua relação de parâmetros). Você deve preencher o corpo das funções solicitadas. Funções auxiliares adicionais podem também ser escritas.

Modelo SIR Episódico
O modelo SIR foi publicado em 1927 por Kermack e McKendrick (Proc. R. Soc. Lond. A, 115:700-721). Ele é um modelo determinístico relativamente simples utilizado até hoje para estimar a evolução de epidemias.

Em sua forma original, o modelo considera três variáveis básicas S, I e R que representam, respectivamente, indivíduos Suscetíveis mas ainda não infectados, indivíduos Infectados (ou seja, doentes) e indivíduos Recuperados, que são removidos do modelo (ou seja, que tiveram a doença no passado e agora não mais a transmitem – porque se curaram e adquiriram imunidade ou porque faleceram). Ele considera, ainda, uma população fixa sob análise de N indivíduos e duas constantes β e γ que representam, respectivamente, fatores de infecção e de recuperação característicos da doença.

Com estes parâmetros (β e γ), o modelo descreve a evolução temporal das variáveis S, I e R usando equações diferenciais codependentes:

dSdt=−βSINdIdt=βSIN−γIdRdt=γI
.

Este modelo não é suficiente para descrever em detalhes a evolução de uma epidemia como, por exemplo, a de COVID-19 que estamos vivenciando. Ele serve, entretanto, para descrever em linhas gerais como uma epidemia evolui. Um dos grandes problemas da aplicação do modelo ao caso do COVID-19 é que ele identifica o grupo dos infectados ao dos doentes, mas não prevê a existência dos assintomáticos: indivíduos infectados que contraem o vírus mas não desenvolvem sintomas. Vários estudos de populações bem demarcadas têm apontado que cerca de metade da população infectada adquire imunidade sem apresentar sintomas, mas em presídios norte-americanos que sofreram um teste massivo verificou-se que 96% da população já infectada era de assintomáticos (Daniel P. Oran, AM, Eric J. Topol, MD, Prevalence of Asymptomatic SARS-CoV-2 Infection, Annals of Internal Medicine, 3 Jun 2020).

A população e sua respectiva cardinalidade N deve considerar grupos que tenham possibilidade de contato e os parâmetros β e γ devem corresponder aos valores observados empiricamente e capazes de representar, respectivamente, quão transmissível se apresenta a doença e o tempo requerido para a recuperação de infectados. A transmissibilidade é determinada por características da doença em si e padrões de comportamento da população (distanciamento social, padrões de higiene, etc.). 

Para simular este modelo computacionalmente, pode ser construída uma versão “episódica” em que o tempo é discretizado para poder ser tratado como uma sequência de números naturais (que podem representar, por exemplo, dias). As equações nesta versão “episódica” ficam assim:

S(t+1)=S(t)−βS(t)I(t)NI(t+1)=I(t)+βS(t)I(t)N−γI(t)R(t+1)=R(t)+γI(t)S(0)=N−1,I(0)=1,R(0)=0
.

Neste EP produziremos um simulador SIR episódico e extrairemos alguns dados dele.



Tarefa 1

Construa uma função SIR(N, Beta, Gama, Tmax) que receba como parâmetros:

N, o tamanho da população (int)

Beta, o parâmetro correspondente a quão transmissível é a doença (float)

Gama, o parâmetro correspondente ao tempo necessário para se recuperar da doença (float)

Tmax, o valor máximo para a variável tempo a ser considerado nas simulações (int)

Esta função deverá retornar como resposta três listas contendo Tmax elementos, correspondendo respectivamente às variáveis S, I e R em cada instante de tempo da lista 0, 1, 2, ..., (Tmax-1).



Exemplo de chamada da função SIR no Python Shell: 

>>> S,I,R = SIR(10, 0.5, 0.1, 10)
>>> imprimeLista(S)  # função fornecida pronta no EP3.py
9.0000  8.5500  7.9729  7.2585  6.4138  5.4712  4.4897  3.5445  2.7054  2.0154 
>>> imprimeLista(I)
1.0000  1.3500  1.7921  2.3273  2.9392  3.5879  4.2106  4.7348  5.1004  5.2803 
>>> imprimeLista(R)
0.0000  0.1000  0.2350  0.4142  0.6469  0.9409  1.2997  1.7207  2.1942  2.7042
Tarefa 2

Construa uma função critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta) que receba como parâmetros:

N, Gama e Tmax como na Tarefa 1

Beta_MIN, Beta_MAX e Beta_delta (float) para representar o intervalo de valores
B={βMIN, βMIN+Δ, βMIN+2Δ, ..., βMAX}, sendo Beta_MIN=βMIN, Beta_MAX=βMAX e Beta_delta=Δ.

Esta função deverá retornar como resposta uma lista representando, para cada valor de β dentro do intervalo B, o valor máximo da variável I produzido pela função da Tarefa 1.

Exemplo de chamada da função critic_SIR no Python Shell: 

>>> cSIR = critic_SIR(10, 0.1, 10, 0.05, 0.50, 0.05)
>>>  imprimeLista(cSIR)  # função fornecida pronta no EP3.py
1.0000  1.0000  1.2663  1.7439  2.3103  2.9424  3.6023  4.2421  4.8139  5.2803 


Nas duas próximas tarefas utilizaremos os formatos PGM e PPM para produção de gráficos para apresentar visualmente resultados numéricos. Uma descrição detalhada destes formatos de arquivo, que são utilizados para o armazenamento de imagens, pode ser encontrada no seguinte link: https://www.ime.usp.br/~mac2166/ep3-2020/pgm_ppm.pdf



Tarefa 3

Construa uma função gera_grafico_simples(L) que receba como parâmetro uma lista L de valores (float) e construa um gráfico X-Y em que o eixo Y tenha como limite inferior o valor Y_MIN=0 e como limite superior o inteiro Y_MAX definido pelo teto do valor máximo encontrado em L, e o eixo X tenha como limite inferior o valor X_MIN=0 e como limite superior X_MAX a quantidade de elementos de L menos um. Este gráfico deve apresentar uma representação dos valores em L. O gráfico corresponderá a uma matriz M de dimensão m x n, sendo o número de linhas dado por m = Y_MAX-Y_MIN+1 e o número de colunas dado por n = X_MAX-X_MIN+1=len(L). Os valores da matriz devem ser padronizados como 255 (branco) para pontos que representem os valores contidos na lista L e 0 (preto) para os demais pontos na imagem. Ou seja, cada ponto (x,y) = (k,L[k]) deverá ser registrado em uma posição M[i][j] da matriz, sendo o índice i obtido por arredondamento de Y_MAX-L[k] para o inteiro mais próximo e x=k=j. Além de devolver a matriz resultante, a função deverá gravar o gráfico gerado na matriz M em um arquivo no formato PGM, com o nome padronizado “graf_simples.pgm”.



Exemplo de chamada da função gera_grafico_simples no Python Shell: 

>>> cSIR = critic_SIR(10, 0.1, 10, 0.05, 0.50, 0.05)
>>>  gera_grafico_simples(cSIR)
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 255, 255, 0, 0], [0, 0, 0, 0, 0, 255, 0, 0, 0, 0], [0, 0, 0, 255, 255, 0, 0, 0, 0, 0], [255, 255, 255, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
Abaixo é exibido o conteúdo do arquivo PGM correspondente “graf_simples.pgm”:

P2
10 7
255
     0       0       0       0       0       0       0       0       0       0
     0       0       0       0       0       0       0       0     255     255
     0       0       0       0       0       0     255     255       0       0
     0       0       0       0       0     255       0       0       0       0
     0       0       0     255     255       0       0       0       0       0
   255     255     255       0       0       0       0       0       0       0
     0       0       0       0       0       0       0       0       0       0



Para visualizar a imagem "graf_simples.pgm", você deve rodar seu programa em Python diretamente no seu computador. No VPL não é possível visualizar as imagens. Para visualizar a imagem, você deve abrir o arquivo "graf_simples.pgm" resultante com algum programa de edição/visualização de imagens, com suporte para o formato PGM. Abaixo é mostrado um exemplo de visualização no Gimp, usando cSIR = critic_SIR(100, 0.2, 100, 0.05, 0.90, 0.05) e depois gera_grafico_simples(cSIR).


Construa uma função gera_grafico_composto(S,I,R) que receba como parâmetros três listas de valores (float) e construa um gráfico X-Y em que o eixo Y tenha como limite inferior o valor Y_MIN=0 e como limite superior o inteiro Y_MAX definido pelo teto do valor máximo encontrado em S∪I∪R, e o eixo X tenha como limite inferior o valor X_MIN=0 e como limite superior X_MAX a quantidade de colunas de S menos um. Este gráfico deve apresentar uma representação dos valores em S, I e R, em formato de linhas superpostas com cores distintas. O gráfico deverá ser registrado em um arquivo no formato PPM, com o nome padronizado “graf_composto.ppm”. A função deverá, também, retornar como resposta o conteúdo do arquivo PPM no formato de uma matriz de valores inteiros. Estes valores devem ser também padronizados como:

“255 0 0” (vermelho) para pontos que representem os valores contidos na lista correspondente aos valores de S, 
“0 255 0” (verde) para pontos que representem os valores contidos na lista correspondente aos valores de I, 
“0 0 255” (azul) para pontos que representem os valores contidos na lista correspondente aos valores de R e
“0 0 0” (preto) para os demais pontos na imagem.
No caso de sobreposição das curvas, as cores devem ser somadas (exemplo, sobreposição de S e I gera cor “255 255 0” (amarelo)).

Exemplo de chamada da função gera_grafico_composto no Python Shell: 
