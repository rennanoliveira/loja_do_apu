from lojinha import Produto
from criador_pedido import CriadorPedido
class Loja:

	def __init__(self):
		self.produtos = []

	def get_produtos(self):
		return self.produtos

	def cadastrar_produto(self, nome, quantidade):
		novo_produto = Produto(nome)
		novo_produto.adicionar_estoque(quantidade)
		self.produtos.append(novo_produto)
		return "Produto Cadastrado: " + novo_produto.get_nome()
		
	def imprime_produtos(self):
		resultado = []
		for produto in self.produtos:
			resultado.append(produto.get_nome() + " (" + str(produto.get_quantidade()) + ")")
		return "Produtos na Loja: " + str(resultado)

	def adicionar_carrinho(self, cliente, nome_produto, quantidade):
		carrinho = cliente.get_carrinho()
		produto = next(x for x in self.produtos if x.get_nome() == nome_produto)
		if(produto.get_quantidade() >= quantidade):
			carrinho.adicionar_produto(produto, quantidade)
			return "Adicionando o produto " + produto.get_nome() + " ao carrinho de " + cliente.get_nome()
		else:
			return "Quantidade solicitada (%s) do produto '%s' menor que a quantidade em estoque (%s)" % (quantidade, nome_produto, produto.get_quantidade())

	def fechar_pedido(self, cliente):
		criador_pedido = CriadorPedido(cliente, self)
		if criador_pedido.save():
			return "Pedido fechado!"
		else: 
		    return "Nao foi possivel fechar o pedido: %s" % (str(criador_pedido.errors))

	def remover_estoque(self, produto, quantidade):
		produto_em_estoque = next(x for x in self.produtos if x.get_nome() == produto.get_nome())
		produto_em_estoque.remover_estoque(quantidade)

	def remover_do_carrinho(self, cliente, nome_produto):
		carrinho = cliente.get_carrinho()
		carrinho.remover_produto(nome_produto)
		return "Produto removido: %s" % nome_produto


		



