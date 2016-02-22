from interface import Loja
from lojinha import Carrinho, Cliente, Produto

# Inicializa a loja, um objeto para substituir a interface do usuario
loja = Loja()

# Criando 4 produtos diferentes.
print loja.cadastrar_produto("Cerveja DUFF", 3)
print loja.cadastrar_produto("Sofa", 2)
print loja.cadastrar_produto("Chupeta", 1)
print loja.cadastrar_produto("Neuronios", 0)

print loja.imprime_produtos()

# Inicializando dois clientes. Homer e Maggie

maggie = Cliente("Maggie Simpson")
homer = Cliente("Homer Simpson")

print maggie.get_nome()
print homer.get_nome()

# Cliente Homer vai solicitar alguns produtos

print loja.adicionar_carrinho(homer, "Cerveja DUFF", 2)
print homer.meu_carrinho()
print loja.adicionar_carrinho(homer, "Sofa", 1)
print homer.meu_carrinho()
print loja.adicionar_carrinho(homer, "Chupeta", 1)
print homer.meu_carrinho()

# Imprimindo produtos da loja para confirmar que adicionar ao carrinho nao remove o produto da lista
print loja.imprime_produtos()

# Loja nao permite que usuario adicione um produto que nao esteja em estoque ao carrinho.
print loja.adicionar_carrinho(homer, "Neuronios", 1)
print homer.meu_carrinho()

# Maggie vai solicitar um produto (que ja esta no carrinho de homer, mas ele ainda nao fechou o pedido)

print loja.adicionar_carrinho(maggie, "Chupeta", 1)
print maggie.meu_carrinho()

# Fechando o pedido de Maggie
# print loja.fechar_pedido(maggie)
# print maggie.meu_carrinho()
# print maggie.meus_pedidos()
# print loja.imprime_produtos()

# Homer vai tentar fechar o pedido, mas Maggie pegou a ultima chupeta!

# print loja.fechar_pedido(homer)
# print loja.remover_carrinho(homer, "Chupeta")
# print loja.fechar_pedido(homer)
# print homer.meu_carrinho()
# print homer.meus_pedidos()
# print loja.imprime_produtos()

