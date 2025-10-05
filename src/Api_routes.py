from flask import Flask, render_template
import os
class Api_routes:
    def __init__(self, app=None):
        if app is None:
            self.app = Flask(__name__)
        else:
            self.app = app
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/')
        def home():
            return render_template('index.html', hostname=os.uname().nodename)
        
        @self.app.route('/dados')
        def dados():
            data = {
                "nome": "Lucas",
                "idade": 30,
                "cidade": "São Paulo"
            }
            return render_template('dados.html', data=data)
        
        @self.app.route('/about')
        def about():
            return render_template('about.html')

        @self.app.route('/status')
        def status():
            return {"status": "running"}

    def run(self, debug=True, host='0.0.0.0', port=3000):
        self.app.run(debug=debug, host=host, port=port)