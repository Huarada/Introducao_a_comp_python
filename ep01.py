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
  Turma: Turma 8
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
#
#   M A I N 
#
# ======================================================================

def main():
   import math
   modo= int(input("modo: "))
   if (modo == 2):
    
      n = int(input("n: "))
      c=0
      n1=0
      n2=0
      n3=0
      n4=0
      s=0
      v=0
      i=0
      #tratamento do problema 2
      while s < n and i< int(math.sqrt(n)) :
          #linhas de codigo para descobrir os numeros primos no intervalo dado
          primo = False
          c=0
          a=0
          while (a < i) and (i%2 !=0 or i ==2) and (i%3 !=0 or i ==3) and (i%5 !=0 or i ==5): #os "and" foram utilizados para agilizar o interpretador, pois  desnecessario incluir multiplos de 2,3, e 5
              a+=1
              if (i%a ==0):
                 c+=1
          if(c==2):
             primo = True

          if primo: #procedimentos de armazenamento dos primos, assim como as contas exigidas pelo problema
              if (v % 4 == 0):
                  n1=i

              if (v % 4 == 1):
                  n2=i

              if (v%4 == 2):
                  n3=i
            
              if(v%4 == 3):
                  n4=i
               
              s = n1*n1 + n2*n2 + n3*n3 + n4*n4
              v+=1
          i+=1
       
      if(s == n) and s!=0:
         n1salvo = n1
         n2salvo = n2
         n3salvo = n3
         n4salvo = n4
        #codigos necessarios para ordenar os n em ordem crescente
         if(n1>n2):
            n4 = n1salvo
            n3 = n4salvo
            n2 = n3salvo
            n1 = n2salvo
      
         elif(n2>n3):
            n1 = n3salvo
            n2 = n4salvo
            n3 = n1salvo
            n4 = n2salvo

         elif(n3>n4):
            n1 = n4salvo
            n2 = n1salvo
            n3 = n2salvo
            n4 = n3salvo
            
         print(n1,n2,n3,n4)

      else:
         print("falso")

   #caso o usuario queira o modo 1
      
   elif(modo == 1):
       #nao foram utilizadas as mesmas variaveis do modo 2, pois, assim, elimina-se qualquer possibilidade de interferencia entre os modos (se existirem)
       nu1 = int(input("n1: "))
       nu2 = int(input("n2: "))
       nu3 = int(input("n3: "))
       nu4 = int(input("n4: "))
       nu  = int(input("n: "))
       #variavel "conta" criada para armazenar o valor do calculo exigido
       conta = nu1*nu1 + nu2*nu2 + nu3*nu3 + nu4*nu4
    
       if(conta == nu):
           print("verdadeiro")

       else:
           print("falso")
main()

        
