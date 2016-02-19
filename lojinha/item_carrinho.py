class ItemCarrinho:

    def __init__(self, produto, qtd):
        self.produto = produto
        self.quantidade = qtd

    def get_produto(self):
    	return self.produto.get_nome()

    def get_quantidade(self):
    	return self.quantidade