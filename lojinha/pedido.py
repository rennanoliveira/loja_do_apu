from datetime import datetime

class Pedido:

    def __init__(self):
        self.produtos = []
        self.codigo = codigo_pedido(self)
        self.data = datetime.now()