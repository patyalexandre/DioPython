# -*- coding: utf-8 -*-
"""19Desafio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TjjKCIsDBUslsSEOlJokn2papDSU8nV8

## Sistema bancário
"""

menu = '''
Menu
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 0 #depositos precisam ser em valores inteiros positivos
limite = 500 #limite diário por saque
numero_saques = 1 
limite_saques = 3 #qte maxima (vlr cte)
extrato = '' #será do tipo string (precisa ter o R$)


#1a parte - acesso ao menu
while True: #loop infinito (pra ter o break)
  
  opcao = input(menu)

  if opcao =='d':
    valor = float(input('Qual o valor para deposito? '))
    if valor>0:
      saldo+= valor
      extrato+= f'Depósito: R$ {valor:.2f}\n'
      print('Depósito realizado!')
    else:
      print('Valor inválido!')

  elif opcao =='s':
    valor = float(input('Qual o valor para saque? '))
    if numero_saques <= limite_saques:
      if valor>0:
        if saldo-valor>0:
          saldo-=valor
          extrato+= f'Saque: R$ {valor:.2f}\n'
          print(f'Saque {numero_saques}/{limite_saques} realizado!')
          numero_saques+=1
        else:
          print('Valor não disponível')
      else:
        print('Valor inválido!') 
    else:
      print('Número de saques extrapolado!')

  elif opcao =='e':
    print('\n*************EXTRATO*************')
    if extrato != '':
      print(extrato)
      print(f'Saldo de {saldo:.2f}')
    else:
      print('Sem movimentações.')
    print('\n*********************************')
  
  elif opcao =='q':
    break
  
  else:
    print('Operação inválida!')