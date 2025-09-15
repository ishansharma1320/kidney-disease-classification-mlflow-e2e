import os
from dotenv import load_dotenv
load_dotenv()
os.environ["KAGGLE_USERNAME"]= os.getenv("username")
os.environ["KAGGLE_KEY"]= os.getenv("key")
import zipfile
import kaggle
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
import subprocess
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.dataset
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            subprocess.run(["kaggle", "datasets" ,"download", f"{dataset_url}","-p",f"{zip_download_dir}","--unzip"], check=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # file_id = dataset_url.split("/")[-2]
            # prefix = 'https://drive.google.com/uc?/export=download&id='
            # gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        