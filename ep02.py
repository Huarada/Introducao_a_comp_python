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

  Nome :Lucas Harada
  NUSP : 11449492
  Turma: Turma 08
  Prof.: Paulo Andre Vechiatto de Miranda

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente  neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================
def polinomioComRaiz(p,b):
    """Devolve True se b é raiz do polinômio representado pela lista p, 
       ou False no caso contrário.
       
       p -- a lista dos coeficientes do polinômio       
       b -- o número a ser testado como raiz
    """
    
    # Escreva aqui o corpo da função

    i= 0
    f = 0.0
    while i <  int(len(p)) :
       f = f + p[i]*(b**i)
       i += 1
    if (f == 0): #  Ajuste o valor de retorno 
       return True

    else:
       return False


# ======================================================================

def polinomioQuociente(p,b):    
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(x-b), onde p(x) é o polinômio cujos coeficientes estão na 
       lista p e b é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido      
       b -- a raiz a ser usada como divisor
    """
    
    # Escreva aqui o corpo da função
    
    # Escreva aqui o corpo da função


    for i in range(len(p) -1,0,-1):
       p[i-1] += p[i]*b
    del p[0]
    return p 
 # ======================================================================
def listaCanonicaDeRaizes(p):    
    """Devolve True se b é raiz do polinômio representado pela lista p, 
       ou False no caso contrário.
       
       p -- a lista dos coeficientes do polinômio       
       b -- o número a ser testado como raiz
    """
    
    # Escreva aqui o corpo da função

    i= 0
    R = []
    b = -100000
    c=0
    g = len(p) - 1
    gcopia = g

    L = list(p)   
    while( b < 10000) and (c < gcopia):
       for j in range(g,0,-1):
           L[j-1] += L[j]*b             #Briot-Ruffini
           
       if( L[0] != 0):
           L = list (p)                 #Reinicia o processo, com um b diferente, caso o b antigo n for raiz
       else:
           c+=1
           R.append(b)
           g -=1                        #Se b for raiz, ele eh guardado em uma lista R. O grau g da funcao decresce, e L eh analisado novamente para descobrir as outras raizes
           b = b -2
           del(L[0])                    #L[0] deletado, pois esse foi o resto do Briot-Ruffini
           p = list(L)
       b+=1


       
    Rcopy = list(R)
    x=0
    z=0
    for k in Rcopy:                   #ordena por valor absoluto
        if k < 0:
            x = R.pop(z)
                                 #retira o valor negativo e o guarda na memoria                            
            for h in R:
                if R.index(h) == (len(R)-1) and abs(x) > h:
                    R.insert(R.index(h)+1,x)
                    break
                if h > 0 and abs(x) <= h :             #analisa o intervalo para realocar o valor negativo
                    if h-1 == abs(x):
                        R.insert(R.index(h)-1,x)     #if necesario para ordenar dois numeros com mesmo valor absoluto. Ex: -2 e 2
                        break
                    else:
                        R.insert(R.index(h),x)
                        break
                    
            z -= 1  
        z +=1  

    return R




# ======================================================================
def polinomioQuocienteRacional(p,b,a):    
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(ax-b) e o resto dessa divisão, onde p(x) é o polinômio 
       cujos coeficientes estão na lista p e b/a é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido
       b -- numerador da raiz a ser usada como divisor
       a -- denominador da raiz a ser usada como divisor
    """
    
    # Escreva aqui o corpo da função

    i= 0
    L = []

    g = len(p) -1
    if (g> 0):
       while i <= g :
    
          L.append(p[i]/a)
          i+=1
       for j in range(g,0,-1):
          L[j-1] +=  L[j]*b/a            #Briot-Ruffini
           
       x = L.pop(0)*a        # consertar as alteracoes do resto causadas pelo ajuste p[j] = n/a

    else:
       L = None
       x = -1

    return(L,x)



# ======================================================================
def listaRaizesRacionais(p):    
    """Devolve True se b é raiz do polinômio representado pela lista p, 
       ou False no caso contrário.
       
       p -- a lista dos coeficientes do polinômio       
       b -- o número a ser testado como raiz
    """
    
    # Escreva aqui o corpo da função

    R = []
    b = -100000
    c=0
    g = len(p) - 1
    gcopia = g

    for a in range (1,20,1):
       L = list(p)
       b = -10000
       D = []
       Dcopy = []
       while( b < 10000) and (c < gcopia):
          for j in range(g,0,-1):
              L[j-1] += L[j]*b/a             #Briot-Ruffini
           
          if( L[0] != 0):
              L = list (p)                 #Reinicia o processo, com um b diferente, caso o b antigo n for raiz
          else:
              c+=1
              D.append(b)
              g -=1                        #Se b for raiz, ele eh guardado em uma lista R. O grau g da funcao decresce, e L eh analisado novamente para descobrir as outras raizes
              b = b -2
              del(L[0])
              p = list(L)
              
          b+=1

       Dcopy = list(D)
       x=0
       z=0
       for k in Dcopy:                   #ordena por valor absoluto
          if k < 0 and len(D)>1 :
              x = D.pop(z)
                                    #retira o valor negativo e o guarda na memoria                            
              for h in D:
                if (D.index(h) == (len(D)-1) and  abs(x) >= abs(h)):
                    D.insert(D.index(h) +1,x)
                    break
                elif  abs(x)<= abs(h) :             #analisa o intervalo para realocar o valor negativo
                    if h-1 == abs(x):
                        D.insert(D.index(h) -1,x)     #if necesario para ordenar dois numeros com mesmo valor absoluto. Ex: -2 e 2
                        break
                    else:
                        D.insert(D.index(h),x)
                        break




              z-=1
          z +=1  
       for v in D:
           R.append(v/a)
    return R 





# ======================================================================
def racionalToString(pn,r):
    """Devolve uma string que apresenta a raiz r do polinômio do qual pn 
       é o coeficiente de maior grau como:
        - um inteiro, caso r seja inteiro
        - na forma b/a, com b e a primos entre si e a > 0, caso contrário

       pn -- coeficiente de maior grau do polinômio
       r -- uma raiz do polinômio
    """
    
    # Escreva aqui o corpo da função
    K = (round(r*pn))
    Kcopia = K
    pncopia = pn
    a =2
    s = 0

    if( abs(r)> 1):
       while a <= abs(Kcopia):
          if (K%a == 0) and (pn%a == 0):
             K = K/a
             pn = pn/a
             a -=1

          if(K%pn ==0):
             K = K/pn
             pn = 1
       
          a+=1
    else:      
       while a <= abs(pn):
          if (K%a == 0) and (pn%a == 0):
             K = K/a
             pn = pn/a
             a -=1

          if(K%pn ==0):
             K = K/pn
             pn = 1
             
       
          a+=1   

       
    if pn ==1:
       V = "%d" %K
    else:
        V = "%d/%d" %(K,pn)
        

    return V      #  Ajuste o valor de retorno 

# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================


# ======================================================================
# FUNÇÕES ADICIONAIS
# Implemente neste bloco as funções adicionais às obrigatórias do EP2.
# Duas funções desse tipo (a polinomioToString e a sig) foram 
# fornecidas no próprio enunciado do EP.
# ======================================================================
def polinomioToString(p):
    """Devolve uma string que representa o polinômio em um formato 
       legível para humanos.
       
       p -- a lista dos coeficientes do polinômio
    """
    n = len(p)-1
    s = ""
    for m in range(n-1):
        if p[n-m] != 0:
            s = "%s%s%dx^%d " % (s, sig(m,p[n-m]), p[n-m], n-m)
    if p[1] != 0:
        s = "%s%s%dx " % (s, sig(n-1,p[1]), p[1])
    if p[0] != 0:
        s = "%s%s%d" % (s, sig(n,p[0]), p[0])
    return s

# ======================================================================
def sig(nTermAnte,coef):
    """Devolve '+' se coef não é negativo e existe termo anterior ao
       termo dele no polinômio. Devolve '' (string vazia) no caso
       contrário. Usado para determinar se o '+' deve aparecer antes
       de coef na string que representa o polinômio.
       
       nTermAnte -- expoente de x no termo anterior ao termo do coef
       coef -- coeficiente de um termo do polinômio 
    """
    if nTermAnte > 0 and coef >= 0:
        return "+"
    else:
        return ""

# ======================================================================
# FIM DO BLOCO DE FUNÇÕES ADICIONAIS
# ======================================================================


# ======================================================================
# FUNÇÃO MAIN 
# Escreva dentro da função main() o código que quiser para testar suas 
# demais funções.
# Somente dentro da função main() você pode usar as funções print e
# input.     
# O código da função main() NÃO será avaliado.
# ======================================================================
def main():
    n = int(input("Digite o grau: "))
    
    # Lê os coeficientes do polinômio
    p = []
    for i in range(n+1):
        p.append(float(input("Digite p["+str(i)+"]: ")))
        i += 1
        
    # Obtém a lista de raízes
    if p[n] == 1:
        raizes = listaCanonicaDeRaizes(p)
        print( 'A lista canonica das raizes inteiras de p(x) =',
               polinomioToString(p), 'eh:')
    else:
        raizes = listaRaizesRacionais(p)
        print( 'A lista canonica das raizes racionais de p(x) =',
               polinomioToString(p), 'eh:')
    
    # Imprime a lista canônica de raízes
    for raiz in raizes:
        s = racionalToString(p[n],raiz)
        print(s, end=" ")
        
    print()
        
                
# ======================================================================
# FIM DA FUNÇÃO MAIN 
# ======================================================================


# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================

