# Homologação de modelo de substituição de alimentos NHAM para recomendação de um item
[![python-version-3.8](https://badgen.net/badge/Python/3.8?color=green)](https://www.python.org/downloads/release/python-380/)



O modelo definido nesse repositório se refere ao mapeamento de alimentos que possam ser substituidos na composição de refeições de um cardápio escolar.


## Sobre o modelo

O sistema de recomendação baseado em k-NN (k-vizinhos mais próximos) adota uma abordagem diferente para sugerir substitutos de ingredientes, considerando a similaridade nutricional entre os itens. Cada item é representado por um vetor de quatro campos, que expressam as quantidades de calorias, proteínas, lipídios e carboidratos.

O algoritmo k-NN utilizado calcula os vizinhos mais próximos de um item específico, levando em conta não apenas as diferenças absolutas entre os valores nutricionais, mas também a importância relativa de cada macronutriente. A métrica de distância utilizada é a distância euclidiana quadrática, que é calculada como a raiz do somatório das diferenças quadradas normalizadas entre os macronutrientes.

O diferencial deste algoritmo reside nos pesos associados a cada campo do vetor, refletindo a importância atribuída a cada macronutriente na comparação entre itens. Os pesos atuais são [3, 2, 1.2, 1], indicando que calorias têm o maior peso (3), seguido por proteínas (2), lipídios (1.2) e carboidratos (1). Esses pesos são fundamentais para a métrica de distância, influenciando a priorização dos itens com base na relação distância * peso. Itens que possuem uma relação menor são considerados mais similares, levando a recomendações mais alinhadas com as preferências nutricionais específicas.

Para avaliar a similaridade entre o item de interesse e as recomendações disponíveis, utilizamos uma tabela de frequência. Nesta tabela, as recomendações que apresentam valores de distância menores em relação ao item a ser substituído são associadas a um intervalo de frequência específico, expresso em quartis. Esses quartis são então correlacionados a valores de cores em um esquema semafórico, onde a cor verde indica uma maior similaridade e, consequentemente, uma recomendação mais forte. Por outro lado, tons mais próximos do vermelho indicam menor similaridade e, por conseguinte, um índice de recomendação mais baixo para os alimentos dentro de um determinado grupo. Essa abordagem com semáforo proporciona uma representação visual intuitiva da afinidade nutricional entre os itens, facilitando a interpretação e seleção de substitutos adequados com base em preferências específicas.

Para acessar a base de dados, o sistema inicia consultando a tabela "item_reference", que contém os itens de referência ligados à tabela TACO. Em seguida, a lista de recomendações para cada item é obtida na tabela "recommendation". Esse processo fornece um mecanismo robusto para identificar substitutos de ingredientes com base em critérios nutricionais específicos e preferências de peso atribuídas a cada macronutriente.

Os item da tabela item_reference são os seguintes:

    codigo = código do item (TACO/IBGE) "code"
    nome = nome do item (TACO) "description"
    grupo = grupo ao qual o item pertence (ANALISADO)
    caloria = calorias_g (TACO)
    proteina = proteínas_g (TACO)
    lipidio = lipídios_g (TACO)
    carboidrato = carboidrato_g (TACO)
    sodium_mg = sódio_mg (TACO)
    potassium_mg = potássio_mg (TACO)
    calcium_mg = cálcio_mg (TACO)
    fiber_g = fibra_g (TACO)
    gramsPortion = 100 gramas por porção

  

Os item da tabela recommendation são os seguintes:

	item_codigo = código do item (TACO/IBGE) "code"
	item_nome nome do item (TACO) "description"
	score = similaridade com o item_reference 
	normalized_score = score normalizado (MinMaxScaler)
	traffic_light_color = cor do semáforo

 

  ## ⚠️!!! AVISO !!!⚠️

Essa aplicação ainda não está pronta para produção as seguintes atividades ainda precisam ser realizadas:

- [ ] Conexão com base de dados do TAG (MySql) -> !!! arquivo dump (Model\dump-TAGDatabase.sql);
- [ ] Modelagem do front-end em php para consultar a base de dados item_reference -> recommendation


