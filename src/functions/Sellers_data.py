import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as px_go

class Sellers_data:
    def __init__(self, csv_path):
        # Verifica se o arquivo existe antes de tentar ler
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")
        self.df = pd.read_csv(csv_path)

    def total_sellers(self):
        """Retorna o número total de sellers."""
        return self.df['seller_id'].nunique()

    def sellers_by_state(self):
        """Retorna a contagem de sellers por estado."""
        return self.df['seller_state'].value_counts()
    
    def get_mergeable_sellers_with_orders_items_and_products(self):
        """Retorna um DataFrame resultante do merge entre sellers, orders, order_items e products."""

        sellers = pd.read_csv('data/olist_sellers_dataset.csv')
        order_items = pd.read_csv('data/olist_order_items_dataset.csv')
        products = pd.read_csv('data/olist_products_dataset.csv')

        merged_df = sellers.merge(order_items, on='seller_id', how='inner').merge(products, on='product_id', how='inner').drop_duplicates()
        
        print(merged_df.head())
        
        return merged_df
    
    def sellers_products_summary(self):
        """Resumo dos produtos vendidos por seller (quantidade e categorias)."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        return merged.groupby('seller_id')['product_id'].nunique().reset_index(name='total_produtos')

    def sellers_categories(self):
        """Categorias de produtos vendidas por seller."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        return merged.groupby('seller_id')['product_category_name'].unique().reset_index(name='categorias')

    def sellers_avg_price(self):
        """Preço médio dos produtos vendidos por seller."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        return merged.groupby('seller_id')['price'].mean().reset_index(name='preco_medio')

    def sellers_total_freight(self):
        """Valor total de frete por seller."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        return merged.groupby('seller_id')['freight_value'].sum().reset_index(name='frete_total')

    def sellers_city_state(self):
        """Retorna seller_id, cidade e estado únicos."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        return merged[['seller_id', 'seller_city', 'seller_state']].drop_duplicates()

    def sellers_products_details(self, seller_id):
        """Retorna detalhes dos produtos vendidos por um seller específico."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        return merged[merged['seller_id'] == seller_id][[
            'product_id', 'product_category_name', 'product_name_lenght',
            'product_description_lenght', 'product_photos_qty',
            'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'
        ]].drop_duplicates()

    def sellers_shipping_stats(self):
        """Estatísticas de prazo de envio por seller."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        merged['shipping_limit_date'] = pd.to_datetime(merged['shipping_limit_date'])
        stats = merged.groupby('seller_id')['shipping_limit_date'].agg(['min', 'max', 'count']).reset_index()
        stats.rename(columns={'min': 'primeiro_envio', 'max': 'ultimo_envio', 'count': 'total_envios'}, inplace=True)
        return stats
    
    def best_products_sold(self, top_n=10):
        """Retorna os produtos mais vendidos por quantidade."""
        merged = self.get_mergeable_sellers_with_orders_items_and_products()
        top_products = merged.groupby('product_category_name').size().reset_index(name='quantidade_vendida')
        return top_products.sort_values(by='quantidade_vendida', ascending=False).head(top_n)

    def get_sellers_dashboard_html(sellers, limit=150):
        """Gera gráficos em HTML para o dashboard dos sellers, mostrando ranking dos maiores valores."""

        # Ranking de vendedores por estado
        df_states = sellers.sellers_by_state().reset_index()
        df_states.columns = ['seller_state', 'count']
        df_states = df_states.sort_values('count', ascending=False).head(limit)
        fig_estado = px.bar(
            df_states,
            x='seller_state', y='count',
            labels={'seller_state': 'Estado', 'count': 'Quantidade'},
            title=f'Top Estados com mais vendedores'
        )
        graph_html = fig_estado.to_html(full_html=False)

        # Ranking de produtos vendidos por seller
        df_produtos = sellers.sellers_products_summary().sort_values('total_produtos', ascending=False).head(limit)
        fig_produtos = px.bar(
            df_produtos,
            x='seller_id', 
            y='total_produtos', 
            labels={'seller_id': 'Seller ID', 'total_produtos': 'Total de Produtos'}, 
            title=f'Top {limit} vendedores por Total de Produtos Vendidos')
        produtos_html = fig_produtos.to_html(full_html=False)

        # Ranking de preço médio por seller
        df_preco = sellers.sellers_avg_price().sort_values('preco_medio', ascending=False).head(limit)
        fig_preco = px.bar(
            df_preco,
            x='seller_id',
            y='preco_medio',
            labels={'seller_id': 'Seller ID', 'preco_medio': 'Preço Médio'},
            title=f'Top {limit} vendedores por Preço Médio')
        preco_html = fig_preco.to_html(full_html=False)

        # Ranking de frete total por seller
        df_frete = sellers.sellers_total_freight().sort_values('frete_total', ascending=False).head(limit)
        fig_frete = px.bar(
            df_frete,
            x='seller_id',
            y='frete_total',
            labels={'seller_id': 'Seller ID', 'frete_total': 'Frete Total'},
            title=f'Top {limit} vendedores por Frete Total')
        frete_html = fig_frete.to_html(full_html=False)

        # Ranking de quantidade de categorias vendidas por seller
        df_categorias = sellers.sellers_categories()
        df_categorias['num_categorias'] = df_categorias['categorias'].apply(lambda x: len(x) if isinstance(x, (list, tuple)) else 0)
        df_categorias = df_categorias.sort_values('num_categorias', ascending=False).head(limit)
        fig_categorias = px.bar(
            df_categorias,
            x='seller_id',
            y='num_categorias',
            labels={'seller_id': 'Seller ID', 'num_categorias': 'Número de Categorias'},
            title=f'Top {limit} vendedores por Diversidade de Categorias')
        categorias_html = fig_categorias.to_html(full_html=False)

        # Ranking de total de envios por seller
        df_envio = sellers.sellers_shipping_stats().sort_values('total_envios', ascending=False).head(limit)
        fig_envio = px.bar(
            df_envio,
            x='seller_id',
            y='total_envios',
            labels={'seller_id': 'Seller ID', 'total_envios': 'Total de Envios'},
            title=f'Top {limit} vendedores por Total de Envios')
        envio_html = fig_envio.to_html(full_html=False)

        # Ranking de cidades com mais sellers
        df_cidade = sellers.sellers_city_state().groupby('seller_city')['seller_id'].nunique().reset_index(name='total_sellers')
        df_cidade = df_cidade.sort_values('total_sellers', ascending=False).head(limit)
        fig_cidade = px.bar(
            df_cidade,
            x='seller_city',
            y='total_sellers',
            labels={'seller_city': 'Cidades', 'total_sellers': 'Total de vendedores'},
            title=f'Top {limit} Cidades com Mais vendedores')
        cidade_html = fig_cidade.to_html(full_html=False)

        #ranking de produtos mais vendidos
        df_best_products = sellers.best_products_sold(top_n=limit)
        fig_best_products = px.bar(
            df_best_products,
            x='product_category_name',
            y='quantidade_vendida',
            labels={'product_category_name': 'Categoria do Produto', 'quantidade_vendida': 'Quantidade Vendida'},
            title=f'Top {limit} Produtos Mais Vendidos por Categoria')
        best_products_html = fig_best_products.to_html(full_html=False)


        return {
            'graph_html': graph_html,
            'produtos_html': produtos_html,
            'preco_html': preco_html,
            'frete_html': frete_html,
            'categorias_html': categorias_html,
            'envio_html': envio_html,
            'cidade_html': cidade_html,
            'best_products_html': best_products_html
        }
    
    def get_sellers_details_html(sellers, seller_id):
        """Gera gráficos em HTML com detalhes de um seller específico."""

        # Detalhes do seller
        info = sellers.sellers_products_details(seller_id)

        if info.empty:
            info_html = f"<h4>Nenhum dado encontrado para o Seller ID: <span class='text-danger'>{seller_id}</span></h4>"
            return info_html
        
        #gerar tabela html
        table_fig = px_go.Figure(
            data=[px_go.Table(
                header=dict(values=["Produto ID", "Categoria do Produto", "Tamanho do Nome do Produto",
                                    "Tamanho da Descrição do Produto", "Quantidade de Fotos do Produto",
                                    "Peso do Produto (g)", "Comprimento do Produto (cm)",
                                    "Altura do Produto (cm)", "Largura do Produto (cm)"],
                            fill_color='#636efa',
                            font=dict(color='white', size=12),
                            align='center',
                            height=30),
                cells=dict(values=[info[col] for col in info.columns],
                           fill_color="#9aa0ff",
                           align='center',
                           font=dict(color='black', size=11)),
                columnwidth=[200, 150, 80, 80, 80, 80, 80, 80, 80]
            )],
            layout=px_go.Layout(margin=dict(l=0, r=0, t=30, b=0))
        )

        info_html = f"<hr><h3>Detalhes dos Produtos do Seller ID: <span class='text-primary'>{seller_id}</span></h3>" + table_fig.to_html(full_html=True, include_plotlyjs='cdn')
        return info_html