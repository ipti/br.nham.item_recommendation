import json
import os

# Obtém o caminho absoluto para o arquivo JSON
caminho_arquivo_json = os.path.realpath(os.path.join(os.path.dirname(__file__), 'taco_data.json'))

# Abre o arquivo JSON
with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)

# Percorre cada objeto no JSON e adiciona o campo "code" com o valor de "id"
for item in dados:
    if "id" in item:  # Verifica se a chave "id" está presente no objeto
        item["id"] = str(item["id"])  # Converte o valor de "id" para string
        item["code"] = item["id"]  # Adiciona o campo "code" com o mesmo valor de "id"
        item["gramsPortion"] = "100"
        item["id"] = int(item["id"])


# Salva o arquivo JSON de volta
with open(caminho_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados, arquivo_json, indent=2)

print("Campo 'code' adicionado com sucesso!")
