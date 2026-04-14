import csv

def extrair_dados(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def transformar(dados):
    for u in dados:
        u["mensagem"] = f"Olá {u['nome']}, sua conta {u['conta']} possui benefícios do cartão {u['cartao']}!"
    return dados

def salvar(dados, caminho):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)

dados = extrair_dados("data/entrada.csv")
dados = transformar(dados)
salvar(dados, "data/saida.csv")

print("ETL concluído!")
