import os
import kagglehub

class Manager_data:

    def download_data():
        """Baixa o dataset do Kaggle usando a biblioteca kagglehub"""

        if not os.path.exists("data"):
            os.makedirs("data")

        print("Baixando dataset do Kaggle...")
        path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
        os.rename(path, "data")
        print("Dataset baixado e salvo em 'data'.")
    
    @staticmethod
    def check_and_install_data():
        """Função de conveniência que mantém a interface original"""
        Manager_data.download_data()