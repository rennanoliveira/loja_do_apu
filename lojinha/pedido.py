from datetime import datetime

class Pedido:

    def __init__(self, produtos):
        self.produtos = produtos
        self.codigo = codigo_pedido(self)
        self.data = datetime.now()
        

    def codigo_pedido(self):
        "1234"