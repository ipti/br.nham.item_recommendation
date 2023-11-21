import pandas as pd
import json

# Abra o arquivo JSON para leitura
with open('csvjson.json', 'r',  encoding='utf-8') as arquivo_json:
    
    # Carregue o conteúdo do arquivo JSON em uma lista de objetos Python
    dados = json.load(arquivo_json)

# Crie listas para armazenar os valores de cada campo
codigos = []
nomes = []
calorias = []
proteinas = []
lipidios = []
carboidratos = []
grupos = []

# Percorra a lista de objetos e adicione os valores dos campos às listas correspondentes
for item in dados:
    codigos.append(item['codigo'])
    nomes.append(item['nome'])
    calorias.append(item['caloria'])
    proteinas.append(item['proteina'])
    lipidios.append(item['lipidio'])
    carboidratos.append(item['carboidrato'])
    grupos.append(item['Grupo'])
dados_convertidos = []

for code, nome, caloria, proteina, lipidio, carboidrato, grupo in zip(codigos, nomes, calorias, proteinas, lipidios, carboidratos, grupos):
    numero_caloria = float(str(caloria).replace(",", "."))
    numero_proteina = float(str(proteina).replace(",", "."))
    numero_lipidio = float(str(lipidio).replace(",", "."))
    numero_carboidrato = float(str(carboidrato).replace(",", "."))
    dados_convertidos.append({'code': code, 'nome': nome, 'caloria': numero_caloria, 'proteina': numero_proteina, 'lipidio': numero_lipidio, 'carboidrato': numero_carboidrato, 'grupo': grupo})

# Salva os dados convertidos em um arquivo JSON
with open('dados_convertidos.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados_convertidos, json_file, ensure_ascii=False, indent=4)
