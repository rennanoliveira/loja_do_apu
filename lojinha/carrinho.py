from item_produto import ItemProduto

class Carrinho:

    def __init__(self):
        self.itens = []

    def get_itens(self):
        return self.itens

    def imprime_produtos(self):
    	resultado = []
    	for item in self.itens:
    		resultado.append(item.get_produto_nome() + "(" + str(item.get_quantidade()) + ")")
    	return resultado

    def adicionar_produto(self, produto, qtd):
    	self.itens.append(ItemProduto(produto, qtd))

    def remover_produto(self, nome_produto):
        item_a_remover = next(x for x in self.itens if x.get_produto_nome() == nome_produto)
        self.itens.remove(item_a_remover)

    def limpar_carrinho(self):
        self.itens = []
