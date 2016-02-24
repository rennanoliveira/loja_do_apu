from interface import Loja
from lojinha import Cliente

# Inicializa a loja, um objeto para substituir a interface do usuario
# loja possui lista de produtos, como nao temos BD para ter de onde buscar os produtos
# loja tambem implementa alguns metodos de interface
print "======== INICIANDO SCRIPT ========"

loja = Loja()

# Criando 4 produtos diferentes.
print "\n======== CRIANDO 4 PRODUTOS DIFERENTES ========"

print loja.cadastrar_produto("Cerveja DUFF", 3)
print loja.cadastrar_produto("Sofa", 2)
print loja.cadastrar_produto("Chupeta", 1)
print loja.cadastrar_produto("Neuronios", 0)

print "\n======== PRODUTOS DISPONIVEIS NA LOJA ========"

print loja.imprime_produtos()

# Inicializando dois clientes. Homer e Maggie
print "\n======== CRIANDO 2 CLIENTES ========"
maggie = Cliente("Maggie Simpson")
homer = Cliente("Homer Simpson")

print maggie.get_nome()
print homer.get_nome()

# Cliente Homer vai solicitar alguns produtos
print "\n======== CLIENTE HOMER ADICIONA PRODUTOS AO CARRINHO ========"

print loja.adicionar_carrinho(homer, "Cerveja DUFF", 2)
print homer.meu_carrinho()
print loja.adicionar_carrinho(homer, "Sofa", 1)
print homer.meu_carrinho()
print loja.adicionar_carrinho(homer, "Chupeta", 1)
print homer.meu_carrinho()

print "\n======== PRODUTOS DISPONIVEIS NA LOJA ========"

# Imprimindo produtos da loja para confirmar que adicionar ao carrinho nao remove o produto da lista
print loja.imprime_produtos()

print "\n======== CLIENTE TENTA ADICIONAR PRODUTO FORA DE ESTOQUE NO CARRINHO ========"
# Loja nao permite que usuario adicione um produto que nao esteja em estoque ao carrinho.
print loja.adicionar_carrinho(homer, "Neuronios", 1)
print homer.meu_carrinho()


print "\n======== CLIENTE MAGGIE SOLICITA PRODUTO (QUE JA ESTA NO CARRINHO DE HOMER) ========"

# Maggie vai solicitar um produto (que ja esta no carrinho de homer, mas ele ainda nao fechou o pedido)
print loja.adicionar_carrinho(maggie, "Chupeta", 1)
print maggie.meu_carrinho()

print "\n======== CLIENTE MAGGIE FECHA SEU PEDIDO ========"

# Fechando o pedido de Maggie
print loja.fechar_pedido(maggie)
print maggie.meu_carrinho()
print maggie.meus_pedidos()

print "\n======== PRODUTOS DISPONIVEIS NA LOJA ========"

print loja.imprime_produtos()

# Homer vai tentar fechar o pedido, mas Maggie pegou a ultima chupeta!
print "\n======== CLIENTE HOMER TENTA FECHAR SEU PEDIDO, MAS MAGGIE JA COMPROU A ULTIMA CHUPETA ========"
print loja.fechar_pedido(homer)


print "\n======== PRODUTOS DISPONIVEIS NA LOJA ========"
print loja.imprime_produtos()

# Homer remove produto em falta
print "\n======== CLIENTE HOMER REMOVE CHUPETA DE SEU CARRINHO ========"
print homer.remover_do_carrinho("Chupeta")

# Homer fecha pedido
print "\n======== CLIENTE HOMER FECHA SEU PEDIDO ========"
print loja.fechar_pedido(homer)
print homer.meu_carrinho()
print homer.meus_pedidos()

print "\n======== PRODUTOS DISPONIVEIS NA LOJA ========"
print loja.imprime_produtos()

