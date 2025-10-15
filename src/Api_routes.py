from flask import Flask, render_template, request
from markupsafe import Markup
from src.functions.Sellers_data import Sellers_data 
import plotly.express as px

class Api_routes:
    def __init__(self, app=None):
        if app is None:
            self.app = Flask(__name__)
        else:
            self.app = app
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/', methods=['GET', 'POST'])
        def home():
            sellers = Sellers_data('data/olist_sellers_dataset.csv')

            if request.method == 'GET':
                dashboard_html = Sellers_data.get_sellers_dashboard_html(sellers)
            elif request.method == 'POST':
                limit = int(request.form.get('limit', 10))
                dashboard_html = Sellers_data.get_sellers_dashboard_html(sellers, limit=limit)

            return render_template(
                'index.html',
                graph_html=Markup(dashboard_html['graph_html']),
                produtos_html=Markup(dashboard_html['produtos_html']),
                preco_html=Markup(dashboard_html['preco_html']),
                frete_html=Markup(dashboard_html['frete_html']),
                envio_html=Markup(dashboard_html['envio_html']),
                cidade_html=Markup(dashboard_html['cidade_html']),
                categorias_html=Markup(dashboard_html['best_products_html'])
            )
        
        @self.app.route('/about_seller', methods=['POST'])
        def about_seller():
            sellers = Sellers_data('data/olist_sellers_dataset.csv')
            data = request.get_json()
            seller_id = data.get('seller_id')
            if not seller_id:
                return f"<h4 class='text-danger text-center'>Erro: Seller ID não fornecido.</h4>"
            
            details_html = Sellers_data.get_sellers_details_html(sellers, seller_id)
            return details_html
            

        @self.app.route('/status')
        def status():
            return {"status": "running"}

    def run(self, debug=True, host='0.0.0.0', port=3000):
        self.app.run(debug=debug, host=host, port=port)