import json

def adicionar_item_id(dados):
    for grupo, grupo_dados in dados.items():
        for item, item_dados in grupo_dados["items"].items():
            item_id = item_dados["item_reference"]["code"]
            for recomendacao in item_dados["recommendations"]:
                recomendacao["id_item"] = item_id


with open('result_data_taco_dados.json', 'r', encoding='utf-8') as arquivo:
    seu_json = json.load(arquivo)

adicionar_item_id(seu_json)

with open('result_data_taco_dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(seu_json, arquivo, indent=4, ensure_ascii=False)
