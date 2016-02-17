class ItemCarrinho:

    def __init__(self, produto, qtd):
        self.produto = produto
        self.quantidade = qtd

    def adicionar(self):
        self.quantidade += 1

    def subtrair(self):
        self.quantidade -= 1
