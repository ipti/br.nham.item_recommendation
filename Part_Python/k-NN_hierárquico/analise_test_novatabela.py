import json


class ItemFinder:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_data(self):
        with open(self.data_file, 'r') as arquivo_json:
            self.dados_json = json.load(arquivo_json)

    def find_item(self, nome, grupo):
        if grupo in self.dados_json:
            for item_nome, item_info in self.dados_json[grupo]["items"].items():
                if item_info["item_reference"]["nome"] == nome:
                    self.print_item_info(item_nome, item_info)
        else:
            print("O grupo não foi encontrado no JSON.")

    def print_item_info(self, item_nome, item_info):
        print("Nome do item:", item_nome)
        print("Recomendações:")
        for recommendation in item_info["recommendations"]:
            self.print_recommendation_info(recommendation)

    def print_recommendation_info(self, recommendation):
        print("- Item name:", recommendation["item_name"][0])
        print("    Score:", recommendation["score"])
        print("    Normalized Score:", recommendation["normalized_score"])
        print("    Traffic Light Color:", recommendation["traffic_light_color"])

