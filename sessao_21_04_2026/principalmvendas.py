# media de vendas da semana

dia1 = 200
dia2 = 320
dia3 = 150
dia4 = 275
dia5 = 300
media_de_vendas = (dia1 + dia2 + dia3 + dia4 +dia5) / 5
print(media_de_vendas)

# verificar se dia foi bom
testar_numero_de_vendas = dia1 - media_de_vendas
if testar_numero_de_vendas > 0:
    print("dia bom")
else:
    print("dia mau")
    


