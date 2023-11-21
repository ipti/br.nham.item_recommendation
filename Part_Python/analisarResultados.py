import json
import random
import os


# Carregue os dados do arquivo JSON
with open('br.nham.model/Part_Python/Arquivos/taco_data_test.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

for group_name, group_data in data.items():
    for item_name, item_data in group_data['items'].items():
        item_reference_id = item_data['item_reference']['id']
        recommendations = item_data['recommendations']

        for recommendation in recommendations:
            recommendation['id_item'] = item_reference_id


with open('br.nham.model/Part_Python/Arquivos/taco_data_test.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)

# Crie um dicionário para armazenar as seleções aleatórias
random_selections = {}

# Agrupe os dados com base nos grupos
grouped_data = {}
for item in data:
    grupo = item['grupo']
    if grupo not in grouped_data:
        grouped_data[grupo] = []
    grouped_data[grupo].append(item)

# Selecione aleatoriamente 5 elementos de cada grupo
for grupo, items in grouped_data.items():
    random_selections[grupo] = random.sample(items, min(5, len(items)))

# Combine as seleções aleatórias de cada grupo, se desejar
all_random_selections = [item for sublist in random_selections.values() for item in sublist]

# Armazene as seleções aleatórias em uma nova estrutura de dados ou arquivo JSON
with open('random_selections.json', 'w', encoding='utf-8') as output_file:
    json.dump(all_random_selections, output_file, indent=4, ensure_ascii=False)

print("Seleções aleatórias foram salvas em random_selections.json")
