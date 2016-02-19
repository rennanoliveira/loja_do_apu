from item_carrinho import ItemCarrinho

class Carrinho:

    def __init__(self):
        self.itens = []

    def imprime_produtos(self):
    	resultado = []
    	for item in self.itens:
    		resultado.append(item.get_produto() + "(" + str(item.get_quantidade()) + ")")
    	return resultado

    def adicionar_produto(self, produto, qtd):
    	self.itens.append(ItemCarrinho(produto, qtd))
    

    def limpar_carrinho(self):
        self.itens = []
