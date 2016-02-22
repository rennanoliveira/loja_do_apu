from datetime import datetime
from item_produto import ItemProduto

class Pedido:

    def __init__(self, cliente):
        self.itens = []
        self.cliente = cliente
        self.codigo = self.codigo_pedido()
        self.data = datetime.now()
        
    def codigo_pedido(self):
        str(datetime.now()) + "1234"

    def adicionar_produto(self, produto, qtd):
    	self.itens.append(ItemProduto(produto, qtd))

    def imprimir_pedido(self):
    	itens_impressos = []
    	for item in self.itens:
    		itens_impressos.append("%s (%s)" % (item.get_produto_nome(), item.get_quantidade()))
    	return str(itens_impressos)