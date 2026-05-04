import minha_funcao

A=True
B=False

Saida = not ((A and not B) or (not A and B ))

Saida = minha_funcao.xnor(A,B)

C = True
D = False

Saida2 = minha_funcao.xnor(C, D)