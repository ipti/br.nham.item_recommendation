import json
import os

class TacoDataProcessor:
    def __init__(self, file_name):
        self.file_path = os.path.realpath(os.path.join(os.path.dirname(__file__), file_name))
        self.data = self.load_data()

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
        return dados

    def process_data(self):
        new_id = 1
        new_data = []

        for d in self.data:
            d["code"] = int(d["code"])
            d["id"] = new_id
            new_id += 1
            new_dict = {"id": d["id"]}
            for key, value in d.items():
                if key != "id":
                    new_dict[key] = value
            new_data.append(new_dict)

        self.data = new_data

    def save_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":

    file_name = 'Arquivos/taco_data_test.json'
    taco_processor = TacoDataProcessor(file_name)
    taco_processor.process_data()
    taco_processor.save_data()
