from lojinha import Carrinho, Cliente, Produto

rafael = Cliente("Rafael")
rennan = Cliente("Rennan")

print rafael.get_nome()
print rennan.get_nome()

monitor = Produto("Monitor")
teclado = Produto("Teclado")
mouse = Produto("Mouse")
cpu = Produto("CPU")
# colocar 5 de cada produto em estoque

# print monitor.verificar_estoque()


print monitor.get_nome()
print teclado.get_nome()
 
print rafael.meu_carrinho()

print rafael.solicitar_produto(monitor, 1)
print rafael.solicitar_produto(teclado, 1)
print rafael.solicitar_produto(mouse, 2)
print rafael.solicitar_produto(cpu, 1)

print rafael.meu_carrinho()

print rafael.limpar_carrinho()

print rafael.meu_carrinho()

rafael.fechar_pedido()
print rafael.meu_pedido()
