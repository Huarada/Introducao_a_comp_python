"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Lucas Harada
  NUSP : 11449492
  Turma: 08
  Prof.: Paulo Andre Vechiatto de Miranda

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""
import math


def SIR (N, Beta, Gama, Tmax) :
    S = [N-1]
    I = [1]
    R = [0]
    Tmax = round(Tmax)
    for i in range (Tmax -1):
        C = Beta*S[i]*I[i]/N
        S.append( S[i] - C)
        I.append(I[i] + C - Gama*I[i])
        R.append(R[i]+ Gama*I[i]) 
        
    return [S,I,R]


def critic_SIR (N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta):
    Beta = Beta_MIN
    I_list = []
    while Beta <= Beta_MAX :
        S,I,R = SIR(N, Beta, Gama, Tmax)
        Imax = 0
        for i in range(len(I)):
            if Imax < I[i]:
                Imax = I[i]
        I_list.append(Imax)        

        Beta = Beta + Beta_delta    
        
        
    return I_list


def gera_grafico_simples(L):
    Lmax = 0
    ListaF = []
    for k in range (len(L)):
        L[k] = round(L[k])
        if Lmax < L[k]:
            Lmax = L[k]

    Lmax = Lmax +1
    for j in range (Lmax,-1, -1):
        Lista = []
        for i in range (len(L)):
            if j == L[i] :
                Lista.append(255)
            else:
                Lista.append(0)
        ListaF.append(Lista)
        
    graf = "graf_simples.pgm"
    grafico = open(graf,'w')
    grafico.write("P2")
    grafico.write('\n')
    Tamanho = str(len(L)) + " " +  str(Lmax+1)
    grafico.write(Tamanho)
    grafico.write('\n')
    grafico.write('255')
    grafico.write('\n')
    for linha in ListaF :
        Texto_linha = ""
        for z in range(len(linha)):
            Texto_linha = Texto_linha + str(linha[z])+ " "
            
        grafico.write(Texto_linha)

        grafico.write('\n')
        
    grafico.close()
        
    return ListaF


def gera_grafico_composto(S, I, R):
    Smax = 0
    Imax = 0
    Rmax = 0
    ListaF = []
    Maximo = 0
    for s in range (len(S)):
        S[s] = round(S[s])
        if Smax < S[s]:
            Smax = S[s]
    for x in range (len(I)):
        I[x] = round(I[x])
        if Imax < I[x]:
            Imax = I[x]
    for r in range (len(R)):
        R[r] = round(R[r])
        if Rmax < R[r]:
            Rmax = R[r]

    if Imax > Smax:              #Ver qual valor é o maximo
        Maximo = Imax
    else:
        Maximo = Smax
        
    if Maximo < Rmax:
        Maximo = Rmax
    Maximo = Maximo
    
    for j in range (Maximo,-1, -1):
        Lista = []
        for i in range (len(S)):
            if j == S[i] :          #teste para S/ vermelho
                Lista.append(255)
            else:
                Lista.append(0)

            if j == I[i]:
                Lista.append(255)
            else:
                Lista.append(0)

            if j == R[i]:
                Lista.append(255)
            else:
                Lista.append(0)
                
            
        ListaF.append(Lista)
        
    graf = "graf_composto.ppm"
    grafico = open(graf,'w')
    grafico.write("P3")
    grafico.write('\n')
    Tamanho = str(len(S)) + " " +  str(Maximo+ 1)
    grafico.write(Tamanho)
    grafico.write('\n')
    grafico.write('255')
    grafico.write('\n')
    for linha in ListaF :
        Texto_linha = ""
        for z in range(len(linha)):
            Texto_linha = Texto_linha + str(linha[z])+ " "
            
        grafico.write(Texto_linha)

        grafico.write('\n')
        
    grafico.close()
    
    return ListaF


def leitura_de_valores(nome_de_arquivo):
    arquivo = open(nome_de_arquivo,'r')
    TEXTO = []
    numero = 0



    for linha in arquivo:
        
        linha = linha.strip()
        
        numero = float(linha)
        TEXTO.append(numero)

    

    return [TEXTO[0], TEXTO[1], TEXTO[2], TEXTO[3], TEXTO[4], TEXTO[5]]


# Opções
# 1: Calcular 'SIR' e imprimir os vetores S, I e R - leitura de teclado
# 2: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de teclado
# 3: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de arquivo
# 4: Calcular 'critic_SIR', testar matriz devolvida por 'gera_grafico_simples' - leitura de teclado
# 5: Calcular 'critic_SIR', testar arquivo PGM no disco por 'gera_grafico_simples' - leitura de teclado
# 6: Calcular 'SIR', testar matriz devolvida por 'gera_grafico_composto' - leitura de teclado
# 7: Calcular 'SIR', testar arquivo PPM no disco por 'gera_grafico_composto' - leitura de teclado

#Não altere as funções abaixo:
def imprimeLista(L) : 
    for i in range(len(L)):
      print("%.4f " % L[i], end=""); # usar apenas 4 digitos apos ponto
    print()

def main():
    Opt = int(input("Digite modo do programa: "))
    if (Opt == 1): # saida - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        print("S = ", end="")
        imprimeLista(S) 
        print("I = ", end="")
        imprimeLista(I)
        print("R = ", end="")
        imprimeLista(R)
    elif (Opt == 2): # saida - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 3): # saida - critic_SIR; entrada - arquivo
        Dados = input("Digite nome do arquivo: "); 
        N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leitura_de_valores(Dados)
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 4): # grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        print(M_grafico)
    elif (Opt == 5): # PGM - grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        g = open("graf_simples.pgm", "r")
        print(g.read())
        g.close()
    elif (Opt == 6): # grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        print(M_grafico)
    elif (Opt == 7): # PPM - grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        g = open("graf_composto.ppm", "r")
        print(g.read())
        g.close()

main()

