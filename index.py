from src.Manager_venv import Manager_venv
import os

def main():
    """Função principal para gerenciar o ambiente virtual e baixar o dataset"""
    Manager_venv.check_and_install_dependencies()

    if not os.path.exists("data"):
        os.makedirs("data")
        from src.Manager_data import Manager_data
        Manager_data.check_and_install_()
    else:
        print("O diretório 'data' já existe. Pulando o download do dataset.")

if __name__ == "__main__":
    main()