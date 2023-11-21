import json
import mysql.connector

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'TAGDatabase',
    'port': 3306
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Caminho do arquivo JSON
json_file_path = 'C:/Users/FabriciaResende-TI/ProjectReact/ProjectTAG02/result_data_taco_dados.json'

# Abrir o arquivo JSON
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Iterar sobre os dados e inserir no banco de dados
for group_name, group_data in data.items():
    for item_id, item_data in group_data['items'].items():
        item_reference = item_data['item_reference']
        codigo = item_reference['code']
        nome = item_reference['nome']
        grupo = item_reference['grupo']
        caloria = item_reference['caloria']
        proteina = item_reference['proteina']
        lipidio = item_reference['lipidio']
        carboidrato = item_reference['carboidrato']
        sodium_mg = item_reference['sodium_mg']
        potassium_mg = item_reference['potassium_mg']
        calcium_mg = item_reference['calcium_mg']
        fiber = item_reference['fiber_g']
        gramsPortion = item_reference['gramsPortion']

        # Comando SQL para inserção
        comando = f'INSERT INTO item_reference (codigo, nome, grupo, caloria, proteina, lipidio, carboidrato, sodium_mg, potassium_mg, calcium_mg, fiber_g, gramsPortion) VALUES ({codigo}, "{nome}", "{grupo}", {caloria}, {proteina}, {lipidio}, {carboidrato}, {sodium_mg}, {potassium_mg}, {calcium_mg}, {fiber}, {gramsPortion})'

        # Executar o comando SQL
        cursor.execute(comando)


# Percorrer todos os itens do JSON e inserir as recomendações na tabela recommendations
for group_name, group_data in data.items():
    for item_id, item_data in group_data['items'].items():
        item_reference = item_data['item_reference']
        item_codigo = item_reference['code']
        recommendations = item_data['recommendations']

        for recommendation in recommendations:
            item_reference_id = recommendation['id_item']
            item_codigo = recommendation['item_name'][1]
            item_nome = recommendation['item_name'][0]
            score = recommendation['score']
            # print(item_reference_id)
            normalized_score = recommendation['normalized_score']
            traffic_light_color = recommendation['traffic_light_color']

            comando = f'INSERT INTO recommendations (item_reference_id, item_codigo, item_nome, score, normalized_score, traffic_light_color) VALUES ({item_reference_id}, {item_codigo}, "{item_nome}", {score}, {normalized_score}, "{traffic_light_color}")'
            cursor.execute(comando)

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()
