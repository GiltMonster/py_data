from src.Manager_venv import Manager_venv
import os

def main():
    """Função principal para gerenciar o ambiente virtual e baixar o dataset"""
    
    Manager_venv.check_and_install_dependencies()

    if not os.path.exists("data"):
        print("O diretório 'data' não existe. Baixando o dataset...")
        from src.Manager_data import Manager_data
        Manager_data.check_and_install_data()
    else:
        print("O diretório 'data' já existe. Pulando o download do dataset.")

    from src.Api_routes import Api_routes
    api = Api_routes()
    api.run()

if __name__ == "__main__":
    main()