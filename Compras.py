# -*- coding: utf-8 -*-
#### Projeto – Lista de Compras
"""
Todos usam um catálogo de itens que serão comprados pelo usuário. É suficiente salvar apenas o nome do item e a quantidade desejada, mas sem que seja permitido dois itens com o mesmo nome. Itens podem ser alterados ou removidos da lista. Itens podem ser marcados como comprados. A lista de itens não é perene, ou seja, os dados só estarão gravados em memória. Quando o programa é finalizado, os itens serão removidos.

Deve ser possível emitir a lista de itens listados por ordem alfabética, com a diferenciação dos itens pendentes (ainda não comprados) dos itens já comprados.
"""

class Compras:
  def __init__(self):
    self.lista = {}

  def __valida_dados(self,nome,quantidade):
    if (nome.isalpha() and quantidade.isdecimal() and int(quantidade) > 0):
      return True
  
  def add_produto(self,produto,quantidade):
    resposta = self.__valida_dados(produto,quantidade)
    if(resposta == True):
      #VERIFICA SE PRODUTO EXISTE      
      if(produto in self.lista):
        self.lista[produto][0] += int(quantidade)
      else:
        self.lista[produto] = [int(quantidade),'Pendente']
    else:
      print('ALERTA: DADOS INCORRETOS')

  def rm_produto(self,produto,quantidade):
    resposta = self.__valida_dados(produto,quantidade)
    if(resposta == True):
      #VERIFICA SE PRODUTO EXISTE
      if(produto in self.lista):
        if(self.lista[produto][0] - int(quantidade) <= 0):
          del self.lista[produto]
        else:
          self.lista[produto][0] -= int(quantidade)
      else:
        print('ALERTA: PRODUTO NÃO EXISTENTE')
    else:
      print('ALERTA: DADOS INCORRETOS')

  def alterar_produto(self,produto,novo_produto):
    if(produto in self.lista):
      self.lista[novo_produto] = self.lista.pop(produto)
    else:
      print('ALERTA: PRODUTO NÃO EXISTE')

  def ver_produtos(self):
    print('{:>4}  {:<24}  {:<8}'.format('QTD', 'NOME DO PRODUTO', 'STATUS'))
    print('===========================================')
    
    if(len(self.lista) == 0):
      print('Lista vazia')
    
    #PRODUTOS COMPRADOS
    for item in sorted(self.lista):
      if(self.lista[item][1] == 'Comprado'):
        print("{:>4}  {:<24}  {:<8}".format(self.lista[item][0],item,self.lista[item][1]))
    
    #PRODUTOS PENDENTES
    for item in sorted(self.lista):
      if(self.lista[item][1] != 'Comprado'):
        print("{:>4}  {:<24}  {:<8}".format(self.lista[item][0],item,self.lista[item][1]))


  def confirmar_compra(self):
    for produto in self.lista:
      self.lista[produto][1] = 'Comprado'
    print('Compra finalizada')

  def ver_instrucoes(self):
    print("Digite uma opção:")
    print("1 - para adicionar produto")
    print("2 - para remover produto")
    print("3 - para alterar nome do produto")
    print("4 - para ver a lista")
    print("5 - para confirmar compra ")
    print("6 - para ver instruções ")
    print("7 - para fechar o programa ")
lista = Compras()
print('LISTA DE COMPRAS')
print('===========================================')
lista.ver_instrucoes()

while True:
  print('===========================================')
  opcao = input('Opção: ')
  print('===========================================')
  
  if (opcao == '1'):  
    nome = input('Adicionar produto: ').capitalize()
    quantidade = input('Quantidade: ')
    lista.add_produto(nome,quantidade)

  elif (opcao == '2'):
    nome = input('Remover produto: ').capitalize()
    quantidade = input('Quantidade: ')
    lista.rm_produto(nome,quantidade)

  elif (opcao == '3'):
    nome = input('Digite o nome atual do produto: ').capitalize()
    novo_nome = input('Digite o novo nome: ').capitalize()
    lista.alterar_produto(nome,novo_nome)

  elif (opcao == '4'):
    lista.ver_produtos()

  elif (opcao == '5'):
    lista.confirmar_compra()

  elif (opcao == '6'):
    lista.ver_instrucoes()

  elif (opcao == '7'):
    print('Programa finalizado')
    break
  else:
    print("ALERTA: DIGITE UM OPÇÃO VÁLIDA")
    lista.ver_instrucoes()