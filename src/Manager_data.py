import os
import kagglehub
import shutil
class Manager_data:

    def download_data():
        """Baixa o dataset do Kaggle usando a biblioteca kagglehub (compatível com Windows e Unix)"""

        if not os.path.exists("data"):
            os.makedirs("data")

        print("Baixando dataset do Kaggle...")
        path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

        if os.path.isdir(path):
            for item in os.listdir(path):
                s = os.path.join(path, item)
                d = os.path.join("data", item)
                if os.path.isdir(s):
                    shutil.move(s, d)
                else:
                    shutil.move(s, d)
            shutil.rmtree(path)
        else:
            shutil.move(path, "data")
        print("Dataset baixado e salvo em 'data'.")
    
    @staticmethod
    def check_and_install_data():
        """Função de conveniência que mantém a interface original"""
        Manager_data.download_data()