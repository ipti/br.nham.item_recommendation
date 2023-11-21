from sklearn.preprocessing import MinMaxScaler 
import numpy as np
import json
import os

def calculate_weighted_similarity(item1, item2, attribute_weights):
    # fórmula de similaridade ponderada entre item1 e item2 com base nos pesos dos atributos
    similarity = 0
    for attribute in attribute_weights:
        similarity += attribute_weights[attribute] * (item1[attribute] - item2[attribute]) ** 2
    return similarity


def weighted_knn_recommendation(item_reference, dataset, k, attribute_weights):
    # Filtra o dataset para incluir apenas itens do mesmo grupo que o item de referência
    same_group_items = [item for item in dataset if item['grupo'] == item_reference['grupo'] and item['code'] != item_reference['code']]
    
    # Calcula a similaridade ponderada para todos os itens no mesmo grupo em relação ao item de referência
    weighted_similarities = []
    for item in same_group_items:
        similarity = calculate_weighted_similarity(item_reference, item, attribute_weights)
        weighted_similarities.append((item, similarity))

    # Identifica os k vizinhos mais próximos
    neighbors = sorted(weighted_similarities, key=lambda x: x[1], reverse=True)[:k]
    # Calcula a pontuação ponderada para cada item
    weighted_scores = {}
    for neighbor, similarity in neighbors:
        neighbor_key = (neighbor['nome'], neighbor['code'])  # Usar o nome como chave única (ou outra chave exclusiva)
        for attribute in attribute_weights:
            weighted_scores.setdefault(neighbor_key, 0)
            weighted_scores[neighbor_key] += similarity * attribute_weights[attribute]

    recommendations = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
    return recommendations


def assign_traffic_light_color(score):
    if score >= 0.8:
        return "Verde"  # Boa recomendação
    elif score >= 0.5:
        return "Amarelo"  # Recomendação razoável
    elif score >= 0.3:
        return "Laranja"  # Recomendação razoável/ruim
    else:
        return "Vermelho"  # Recomendação ruim



with open('Part_Python/Arquivos/taco_data_test.json', 'r', encoding='utf-8') as json_file:
    dataset = json.load(json_file)


print('--dataset--', len(dataset))

attribute_weights = {"proteina": 0.4, "carboidrato": 0.3, "lipidio": 0.3, "caloria":0.2}
k = 150

attributes_to_normalize = ["proteina", "carboidrato", "lipidio", "caloria"]
data_to_normalize = [[item[attr] for attr in attributes_to_normalize] for item in dataset]



scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data_to_normalize)
print('--normalizados--', len(normalized_data))

for item in dataset:
    for attr in attributes_to_normalize:
        item[attr] = normalized_data[dataset.index(item)][attributes_to_normalize.index(attr)]
    print(item)

result_dict = {}

for item_reference in dataset:
    if item_reference['grupo'] not in result_dict:
        result_dict[item_reference['grupo']] = {
            'group_reference': item_reference['grupo'],
            'items': {}
        }
       

    recommendations = weighted_knn_recommendation(item_reference, dataset, k, attribute_weights)
    recommendations_dict = {}

    scores = np.array([score for item, score in recommendations]).reshape(-1, 1)
    # print(scores)
    # print('----------------------')

    print((f' Grupo {item_reference["grupo"]}'))
    # print(scores)

    # Menor e maior elemento dos scores dos grupos
    
    # max_score = np.max(scores)
    # min_score = np.min(scores)
    # n = (max_score - min_score)
    # print(f'Valor: {n}')
    # print(f'Menor valor: {min_score}')


    scaler = MinMaxScaler()
    normalized_scores = scaler.fit_transform(scores)
    
    result_dict[item_reference['grupo']]['items'][item_reference['nome']] = {
        'item_reference': item_reference,
        'recommendations': []
    }


    for i, (item, score) in enumerate(recommendations):
        traffic_light_color = assign_traffic_light_color(normalized_scores[i][0])
        item_info = {
            'item_name': item,
            'score': score,
            'normalized_score': normalized_scores[i][0],
            'traffic_light_color': traffic_light_color
        }
        result_dict[item_reference['grupo']]['items'][item_reference['nome']]['recommendations'].append(item_info)



output_file_path = "result_data_taco_dados.json"

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(result_dict, output_file, indent=4, ensure_ascii=False)
output_file.close()

print(f"Os dados foram salvos em {output_file_path}")
