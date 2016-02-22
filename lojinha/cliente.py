from carrinho import Carrinho
class Cliente:

	def __init__(self, nome):
		self.nome = nome
		self.carrinho = Carrinho()

	def get_nome(self):
		return self.nome

	def get_carrinho(self):
		return self.carrinho

	def meu_carrinho(self):
		return "Carrinho de %s: %s" % (self.get_nome(), self.carrinho.imprime_produtos())

	def limpar_carrinho(self):
		self.carrinho.limpar_carrinho()
		return 'Produtos removidos'