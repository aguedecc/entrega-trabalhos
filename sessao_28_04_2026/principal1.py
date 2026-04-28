### - criar uma estrutura de dados com os componentes
# de um quandro eletrico à vossa escolhs.
# menciona as especificações dos componentes
quadro_eletrico ={
    "corte_geral":{
        "in" : 32,
    } 
    {"diferencial":
        "deltaI":0.03,
        "in" : 32
    },
    "disjuntor1":
    {
        "in":10
    }
    "disjuntor2":
    {
        "in" : 16
    }
}

lampadas = {
    "potencia" : 40,
    "tensao" : 230,
    "quantidade" :3
}
def calcular_corrente(potencia, tensao):
    corrente = potencia / tensao
    return corrente

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)
corrente_de_todas_as_lampadas = corrente_de_cada_lampada * lampadas["quantidades"]

if corrente_de_todas_as_lampadas < 6: 
    print("c6")
elif corrente_de_todas_as_lampadas >= 6 and corrente_de_todas_as_lampadas >10:
    print("c10")
elif corrente_de_todas_as_lampadas >= 10 and corrente_de_todas_as_lampadas >16:
    print("c16")
elif corrente_de_todas_as_lampadas >= 16 and corrente_de_todas_as_lampadas >20:
    print("c20")
elif corrente_de_todas_as_lampadas >= 20 and corrente_de_todas_as_lampadas >25:
    print("c26")
    

import minhas_funcoes

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)
corrente_de_cada_lampada = minhas_funcoes.calcular_corrente(lampadas["potencia"], lampadas["tensao"])
print(corrente_de_cada_lampada)

corrente_de_todas_as_lampadas = corrente_de_cada_lampada

minhas_funcoes.selecionar_disjuntor(corrente_de_cada_lampada)