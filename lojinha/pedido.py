from datetime import datetime
from item_produto import ItemProduto

class Pedido:

    SITUACOES = {
    '1': "Aguardando Pagamento",
    '2': "Aguardando Envio",
    '3': "Em Curso",
    '4': "Recebido pelo Cliente"
    }

    def __init__(self, cliente):
        self.itens = []
        self.cliente = cliente
        self.codigo = self.codigo_pedido()
        self.data = datetime.now()
        self.status = self.SITUACOES['1']
        
    def codigo_pedido(self):
        str(datetime.now()) + "1234"

    def adicionar_produto(self, produto, qtd):
    	self.itens.append(ItemProduto(produto, qtd))

    def imprimir_pedido(self):
    	itens_impressos = []
    	for item in self.itens:
    		itens_impressos.append("%s (%s)" % (item.get_produto_nome(), item.get_quantidade()))
    	return str(itens_impressos)
    
    def pagamento_recebido(self):
        self.status = self.SITUACOES["2"]

    def enviado_pelos_correios(self):
        self.status = self.SITUACOES["3"]

    def finalizar(self):
        self.status = self.SITUACOES["4"]

    def status_atual(self):
        return self.status

