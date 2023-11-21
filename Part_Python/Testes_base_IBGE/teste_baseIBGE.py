import json


class ItemFinder:
    def __init__(self, data_file):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        with open(self.data_file, 'r') as arquivo_json:
            self.dados_json = json.load(arquivo_json)

    def find_item(self, data):
        grupo_procurado = data["grupo"]
        if grupo_procurado in self.dados_json:
            for item_nome, item_info in self.dados_json[grupo_procurado]["items"].items():
                if item_info["item_reference"]["nome"] == data["nome"]:
                    return self.format_item_info(item_nome, item_info)
        else:
            return "O grupo não foi encontrado no JSON."

    def format_item_info(self, item_nome, item_info):
        info = {
            "Nome do item": item_nome,
            "Recomendações": []
        }
        for recommendation in item_info["recommendations"]:
            info["Recomendações"].append(self.format_recommendation_info(recommendation))
        return info

    def format_recommendation_info(self, recommendation):
        return {
            "Item name": recommendation["item_name"][0],
            "Score": recommendation["score"],
            "Normalized Score": recommendation["normalized_score"],
            "Traffic Light Color": recommendation["traffic_light_color"]
        }

