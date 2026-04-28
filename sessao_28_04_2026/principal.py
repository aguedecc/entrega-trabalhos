### - criar uma estrutura de dados com os componentes
# de um quandro eletrico à vossa escolhas.
# menciona as especificações dos componentes

{
  "quadro_eletrico": {
    "tipo": "Residencial de Embutir",
    "material": "Termoplástico autoextinguível",
    "protecao_ip": "IP40",
    "componentes": [
      {
        "nome": "Corte Geral (Interruptor Seccionador)",
        "funcao": "Isolamento total da instalação",
        "especificacoes": {
          "corrente_nominal": "40A ou 63A",
          "polos": "4P (Trifásico + Neutro)",
          "tensao": "400V AC"
        }
      },
      {
        "nome": "Descarregador de Sobretensões (DST/SPD)",
        "funcao": "Proteção contra picos de tensão (trovoadas)",
        "especificacoes": {
          "classe": "Tipo 2",
          "corrente_descarga_max": "20kA",
          "tensao_max_servico": "275V"
        }
      },
      {
        "nome": "Interruptor Diferencial (ID)",
        "funcao": "Proteção de pessoas contra choques elétricos",
        "especificacoes": {
          "sensibilidade": "30mA (Alta sensibilidade)",
          "classe": "Tipo A (imunizado)",
          "corrente_nominal": "40A"
        }
      },
      {
        "nome": "Disjuntor Magnetotérmico (MCB) - Cozinha",
        "funcao": "Proteção do circuito de eletrodomésticos",
        "especificacoes": {
          "corrente_nominal": "16A",
          "curva_disparo": "Curva C",
          "poder_corte": "6kA"
        }
      },
      {
        "nome": "Disjuntor Magnetotérmico (MCB) - Iluminação",
        "funcao": "Proteção do circuito de luzes",
        "especificacoes": {
          "corrente_nominal": "10A",
          "curva_disparo": "Curva C",
          "seccao_cabo_recomendada": "1.5mm²"
        }
      },
      {
        "nome": "Barramento de Pente (Fase/Neutro)",
        "funcao": "Interligação segura entre disjuntores",
        "especificacoes": {
          "tipo": "Isolado",
          "passo": "18mm (1 módulo DIN)"
        }
      }
    ]
  }