import json

# Ler os dados de entrada
with open('entrada.json', 'r') as input_file:
    data = json.load(input_file)

with open('result_data.json', 'r') as input_file:
    result = json.load(input_file)

output_data = {}

for item in data:
    
    grupo = item["grupo"]
    code = item["nome"]

    if grupo in result:

        print('\n --------------------------------')
        print(f"Grupo {grupo} encontrado no Código 2")
        items = result[grupo]["items"]
        print("Itens:")
        for item_name, item_data in items.items():
            count = 0
            if item_name == code:
                print(f"Item encontrado: {code}")
                recommendations_data = []

                for recommendation in item_data['recommendations']:
                    recommended_item_name = recommendation['item_name'][0]
                    if recommended_item_name in [i["nome"] for i in data]:
                        print(f"Recomendado: {recommended_item_name}")
                        print("Dados de recomendação:")
                        print(f"item_name: {recommendation['item_name']}")
                        print(f"score: {recommendation['score']}")
                        print(f"normalized_score: {recommendation['normalized_score']}")
                        print(f"traffic_light_color: {recommendation['traffic_light_color']}")
                        count += 1

                        # Crie um dicionário com os dados de recomendação
                        recommendation_data = {
                            "item_name": recommendation['item_name'],
                            "score": recommendation['score'],
                            "normalized_score": recommendation['normalized_score'],
                            "traffic_light_color": recommendation['traffic_light_color']
                        }
                        recommendations_data.append(recommendation_data)

                if count == 0:
                    print('Recomendações para o item não foram encontradas')

                # se quiser adicionar todos os itens mesmo os que não tem recomendações com o vetor de recomendaçoes vazio
                if count > 0:
                    item_data = {
                        "item_reference": {
                            "grupo": grupo,
                            "nome": code,
                            "code": item_data["item_reference"]["code"]
                        },
                        "recommendations": recommendations_data
                    }

                    if grupo not in output_data:
                        output_data[grupo] = {"group_reference": grupo, "items": {}}
                    output_data[grupo]["items"][code] = item_data

    else:
        print(f"Grupo {grupo} não encontrado no Código 2")

with open('output_data.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=4)
