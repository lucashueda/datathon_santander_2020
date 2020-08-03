# Time 'Zin' Datathon Santander 2020

Solução do time "Zin" no desafio do Santander DataThon 2020.

# Solução

Nossa solução se baseia em duas frentes, atendendo 2 principais dores dos pequenos empreendimentos: **(a) A dificuldade de converter pro ambiente digital e a (b) mudança do perfil de consumo dos consumidores**.

Dessa forma buscamos solucionar (a) através de uma ferramenta que a partir de fotos dos itens da loja do empreendedo automaticamente é gerado uma versão digital de seu inventário. O algoritmo automaticamente reconhece o item e o adiciona em uma base de dados. Essa solução se baseou no fine-tuning de uma rede InceptionV3 em alguns itens previamente escolhidos e "scrappados" pelo bing images. O modelo atingiu 98% de acurácia na validação. 

A partir disso o problema (b) é automaticamente linkado através da nossa solução de identificação do perfil de consumo dos clientes através de uma análise das buscas feitas no google. A solução gera um score de interesse de usuário para cada produto no inventário do comércio, podendo assim direcionar propagandas e ofertas com base no perfil de interesse dos clientes. Essa etapa basicamente calcula a média da derivada da função de interesse pelo api do Google Trends, o que nos da uma interpretação de score de "ascendencia" no interesse dos consumidores.

# Estrutura dos códigos

- main.py : Método que mapeia cada imagem da pasta "test_image" classificando-as e gerando o "inventario.csv" com os itens do inventario
- trends.py : Método que recebe uma lista de itens e já realiza a busca no Google Trends e gerando o score proposto, gerando o arquivo "local_ordered.csv" com a ordenação dos itens procurados


# Link

O entregável é notebook presente no repositório "Notebook final.ipynb" no entanto o mesmo pode ser rodado em tempo real no seguinte link [Colaboratory](https://colab.research.google.com/drive/1mYFF2KMUL0PdqnyMBiCfB34MW1INCNlz?usp=sharing)

# Equipe

- Abelardo Borges Fukasawa (Data Engineer)
- Lucas Hideki Ueda (Data Scientist)
- Victor Wildner (Data Analyst)
- Vivian Estequi (Business Analyst)
- Wesley Rischioni (Colaborador Santander)
