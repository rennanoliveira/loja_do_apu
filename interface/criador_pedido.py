from lojinha import Pedido
class CriadorPedido:

	def __init__(self, cliente, loja):
		self.cliente = cliente
		self.loja = loja
		self.errors = []

	def save(self):
		itens_no_carrinho = self.cliente.get_carrinho().get_itens()
		return (self.verifica_itens(itens_no_carrinho) and self.fechar_pedido(itens_no_carrinho))

	def verifica_itens(self, itens):
		for item in itens:
			produto = next(x for x in self.loja.get_produtos() if x.get_nome() == item.get_produto_nome())
			if(produto.get_quantidade() < item.get_quantidade()):
				erro = "Quantidade solicitada (%s) do produto '%s' menor que a quantidade em estoque (%s)" % (item.get_quantidade(), produto.get_nome(), produto.get_quantidade())
				self.errors.append(erro)

		return len(self.errors) == 0

	def fechar_pedido(self, itens):
		novo_pedido = Pedido(self.cliente)
		for item in itens:
			novo_pedido.adicionar_produto(item.get_produto(), item.get_quantidade())
			self.loja.remover_estoque(item.get_produto(), item.get_quantidade())
		self.cliente.limpar_carrinho()
		self.cliente.adicionar_pedido(novo_pedido)
		return True
