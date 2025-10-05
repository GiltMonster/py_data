class Api_routes:
    from flask import Flask

    def __init__(self, app=None):
        if app is None:
            self.app = self.Flask(__name__)
        else:
            self.app = app
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/')
        def home():
            return "Welcome to the API!"
        
        @self.app.route('/status')
        def status():
            return {"status": "running"}

    
    def run(self, debug=True, host='0.0.0.0', port=3000):
        self.app.run(debug=debug, host=host, port=port)