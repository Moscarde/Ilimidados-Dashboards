from etl.etl_linkedin import EtlLinkedin
from datetime import datetime
import os

if __name__ == "__main__":
    if not os.path.exists("linkedin/data/raw/365d"):
        print("Criando diretórios...")
        os.makedirs("linkedin/data/raw/365d")
        os.makedirs("linkedin/data/processed/365d")
        print("Adicione os arquivos de extrações novas em 'etl/linkedin/data/raw/365d/<MES>'")
        print("Adicione os arquivos processados anteriormente em 'etl/linkedin/data/processed/365d/'")
        exit()


    start_time = datetime.now()
    etl = EtlLinkedin()
    extraction_folders = os.listdir(etl.path_etl)
    etl.mass_etl(extraction_folders)
    total_time = datetime.now() - start_time
    print("Total time:", total_time)