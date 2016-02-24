from carrinho import Carrinho
class Cliente:

	def __init__(self, nome):
		self.nome = nome
		self.carrinho = Carrinho()
		self.pedidos = []

	def get_nome(self):
		return self.nome

	def get_carrinho(self):
		return self.carrinho

	def meu_carrinho(self):
		return "Carrinho de %s: %s" % (self.get_nome(), self.carrinho.imprime_produtos())

	def limpar_carrinho(self):
		self.carrinho.limpar_carrinho()
		return 'Produtos removidos'

	def adicionar_pedido(self, pedido):
		self.pedidos.append(pedido)

	def meus_pedidos(self):
		resultado = []
		for pedido in self.pedidos:
			resultado.append(str(pedido.imprimir_pedido()))
		return "Pedidos de %s: %s" % (self.nome, str(resultado))

	def get_pedidos(self):
		return self.pedidos

	def remover_do_carrinho(self, nome_produto):
		self.carrinho.remover_produto(nome_produto)
		return "Produto removido: %s" % nome_produto