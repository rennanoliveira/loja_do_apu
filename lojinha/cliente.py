from carrinho import Carrinho
class Cliente:

	def __init__(self, nome):
		self.nome = nome
		self.carrinho = Carrinho()

	def get_nome(self):
		return self.nome

	def meu_carrinho(self):
		return self.carrinho.imprime_produtos()

	def solicitar_produto(self, produto, qtd):
		self.carrinho.adicionar_produto(produto, qtd)
		return "Produto adicionado: " + produto.get_nome()

	def limpar_carrinho(self):
		self.carrinho.limpar_carrinho()
		return 'Produtos removidos'