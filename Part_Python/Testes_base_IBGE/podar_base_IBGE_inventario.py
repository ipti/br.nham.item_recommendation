import json

class RecommendationProcessor:
    def __init__(self, input_data, result_file, output_file):
        self.data = input_data
        self.result = self.load_data(result_file)
        self.output_data = {}
        self.output_file = output_file

    def load_data(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def process_recommendations(self):
        for group_name, group_items in self.data.items():
            for item in group_items:
                grupo = item["grupo"]
                code = item["nome"]

                if grupo in self.result:
                    print('\n --------------------------------')
                    print(f"Grupo {grupo} encontrado no Código 2")
                    items = self.result[grupo]["items"]
                    print("Itens:")

                    for item_name, item_data in items.items():
                        count = 0

                        if item_name == code:
                            print(f"Item encontrado: {code}")
                            recommendations_data = []

                            for recommendation in item_data['recommendations']:
                                recommended_item_name = recommendation['item_name'][0]

                                if recommended_item_name in [i["nome"] for i in group_items]:
                                    self.print_recommendation_details(recommendation)
                                    count += 1
                                    recommendation_data = self.create_recommendation_data(recommendation)
                                    recommendations_data.append(recommendation_data)

                            if count == 0:
                                print('Recomendações para o item não foram encontradas')

                            if count > 0:
                                item_data = {
                                    "item_reference": {
                                        "grupo": grupo,
                                        "nome": code,
                                        "code": item_data["item_reference"]["code"]
                                    },
                                    "recommendations": recommendations_data
                                }

                                if group_name not in self.output_data:
                                    self.output_data[group_name] = {"group_reference": grupo, "items": {}}
                                self.output_data[group_name]["items"][code] = item_data
                else:
                    print(f"Grupo {grupo} não encontrado no Código 2")

        self.save_output_data()

    def print_recommendation_details(self, recommendation):
        print(f"Recomendado: {recommendation['item_name'][0]}")
        print("Dados de recomendação:")
        print(f"item_name: {recommendation['item_name']}")
        print(f"score: {recommendation['score']}")
        print(f"normalized_score: {recommendation['normalized_score']}")
        print(f"traffic_light_color: {recommendation['traffic_light_color']}")

    def create_recommendation_data(self, recommendation):
        return {
            "item_name": recommendation['item_name'],
            "score": recommendation['score'],
            "normalized_score": recommendation['normalized_score'],
            "traffic_light_color": recommendation['traffic_light_color']
        }

    def save_output_data(self):
        with open(self.output_file, 'w') as output_file:
            json.dump(self.output_data, output_file, indent=4)

if __name__ == '__main__':
    input_data = {
        "escola paulistinha": [
            {
                "nome": "Item 1",
                "grupo": "arroz",
                "code": 1
            },
            {
                "nome": "Item 35",
                "grupo": "massa",
                "code": 35
            },
            {
                "nome": "Item 15",
                "grupo": "massa",
                "code": 15
            }
        ]
    }
    result_file = 'result_data.json'
    output_file = 'output_data.json'

    processor = RecommendationProcessor(input_data, result_file, output_file)
    processor.process_recommendations()
