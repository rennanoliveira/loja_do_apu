class Carrinho:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos << produto

    def limpar_carrinho(self):
        self.produtos = []