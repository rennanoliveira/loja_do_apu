from produto_estoque import ProdutoEstoque
class Produto:

    def __init__(self, nome):
    	self.produtos_estoques = []
        self.nome = nome

    def get_nome(self):
    	return self.nome

    def adicionar_estoque(self, qtd):
    	for _ in range(qtd):
    	  self.produtos_estoques.append(ProdutoEstoque(self))

    def remover_estoque(self, qtd):
        for _ in range(qtd):
            self.produtos_estoques.pop(0)

    def get_quantidade(self):
    	return len(self.produtos_estoques) 