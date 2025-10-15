# Sobre o PY Data

Este repositório contém scripts Python para configurar um ambiente virtual (venv), instalar dependências e baixar um conjunto de dados públicos de e-commerce brasileiro da Olist. O objetivo será de implementar uma pequena API em Flask para trabalhar com esses dados onde além do usu como API - REST, também será possível fazer análises exploratórias e visualizações de dados através do front-end do próprio Flask através de templates HTML.

## Alguns ids de sellers para teste caso queira explorar os dados:

- Seller ID - 01: `4a3ca9315b744ce9f8e9374361493884`
- Seller ID - 02: `cca3071e3e9bb7d12640c9fbe2301306`
- Seller ID - 03: `d91fb3b7d041e83b64a00a3edfb37e4f`
- Seller ID - 04: `fa1e13f2614d7b5c4749cbc52fecda94`
- Seller ID - 05: `7142540dd4c91e2237acb7e911c4eba2`
- Seller ID - 06: `6560211a19b47992c3666cc44a7e94c0`
- Seller ID - 07: `da8622b14eb17ae2831f4ac5b9dab84a`
- Seller ID - 08: `ea8482cd71df3c1969d7b9473ff13abc`
- Seller ID - 09: `3d871de0142ce09b7081e2b9d1733cb1`
- Seller ID - 10: `7c67e1448b00f6e969d365cea6b010ab`

## TO-DO

- [🟢] Configuração do ambiente virtual
- [🟢] Instalação de dependências
- [🟢] Download do conjunto de dados do Kaggle
- [🟢] Implementação de uma API simples em Flask
- [🟢] Análises exploratórias e visualizações de dados no front-end do Flask
- [🔴] Implementação da API - REST completa

## Executando o Projeto

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório:

   ```bash
    git clone https://github.com/GiltMonster/py_data
    cd py_data
    ```

2. Execute o script `index.py` e siga as instruções nele para configurar o ambiente virtual, instalar as dependências e baixar o conjunto de dados do Kaggle. E não se preocupe, esse script criará um ambiente virtual na pasta `venv`, instalará as dependências listadas na classe `Manager_venv` e baixará o conjunto de dados do que vem do [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), salvando-o na pasta `data`.

   ```bash
   python3 index.py #Ou utilize o seu alias caso tenha um
   ```

3. Execute a aplicação Flask, que estará disponível no seu navegador na porta `3000`:

    ```plaintext
    http://localhost:3000/
    ```

---

## Principais bibliotecas utilizadas

- Flask
- Pandas
- Plotly
- Dash
- KaggleHub

## Sobre o Conjunto de Dados de E-commerce Brasileiro da Olist

Bem-vindo! Este é um conjunto de dados públicos de e-commerce brasileiro com pedidos feitos na Loja [Olist](https://www.olist.com/) disponibilizado no [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). O conjunto de dados contém informações de 100 mil pedidos de 2016 a 2018, feitos em diversos marketplaces no Brasil. Seus recursos permitem visualizar um pedido em diversas dimensões: desde o **status do pedido**, **preço**, **pagamento** e **desempenho do frete até a localização do cliente**, **atributos do produto** e, por fim, **avaliações escritas por clientes**. Também foi disponibilizado um conjunto de dados de geolocalização que relaciona CEPs brasileiros às coordenadas de latitude/longitude.

Estes são dados comerciais reais, foram anonimizados e as referências às empresas e parceiros no texto da avaliação foram substituídas pelos nomes das grandes casas de Game of Thrones.

### Contexto

Este conjunto de dados foi generosamente cedido pela Olist, a maior loja de departamentos dos marketplaces brasileiros. A Olist conecta pequenas empresas de todo o Brasil a canais sem complicações e com um único contrato. Esses comerciantes podem vender seus produtos através da Loja Olist e enviá-los diretamente aos clientes usando os parceiros de logística da Olist.

Após a compra de um produto na Loja Olist, o vendedor é notificado para processar o pedido. Assim que o cliente recebe o produto ou a data estimada de entrega se aproxima, ele recebe uma pesquisa de satisfação por e-mail, onde pode registrar sua experiência de compra e fazer alguns comentários.

### Atenção

1. Um pedido pode ter vários itens.
2. Cada item pode ser processado por um vendedor diferente.
3. Todos os textos que identificam lojas e parceiros foram substituídos pelos nomes das grandes casas de Game of Thrones.

#### Exemplo de listagem de produto em um marketplace

![Exemplo de listagem de produto em um marketplace](./assets/example_of_a_product_listing_on_a_marketplace.png)

## Estrutura dos Dados

Os dados estão organizados em 9 arquivos CSV:

- `olist_customers_dataset.csv`: informações sobre os clientes (ID do cliente, localização, etc.).

- `olist_geolocation_dataset.csv`: informações de geolocalização (CEP, cidade, estado, latitude, longitude).

- `olist_order_items_dataset.csv`: informações sobre os itens do pedido (ID do pedido, ID do produto, preço, quantidade, etc.).

- `olist_order_payments_dataset.csv`: informações sobre os pagamentos do pedido (ID do pedido, método de pagamento, valor, etc.).

- `olist_order_reviews_dataset.csv`: informações sobre as avaliações do pedido (ID do pedido, nota, comentário, etc.).

- `olist_orders_dataset.csv`: informações sobre os pedidos (ID do pedido, status, data, etc.).

- `olist_products_dataset.csv`: informações sobre os produtos vendidos pela Olist (ID do produto, nome, categoria, etc.).

- `olist_sellers_dataset.csv`: informações sobre os vendedores (ID do vendedor, localização, etc.).

- `product_category_name_translation.csv`: tradução dos nomes das categorias de produtos do português para o inglês.

## Consulte o esquema de dados

![Esquema de dados](./assets/data_schema.png)
