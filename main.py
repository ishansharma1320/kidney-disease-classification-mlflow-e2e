from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import BaseModelPreparationPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["MLFLOW_TRACKING_URI"]= os.getenv("DAGSHUB_MLFLOW_TRACKING_URI")
os.environ["MLFLOW_TRACKING_USERNAME"]= os.getenv("DAGSHUB_MLFLOW_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"]= os.getenv("DAGSHUB_PAT")

# try:
#         STAGE_NAME = "Data Ingestion Stage"
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# try:
#         STAGE_NAME = "Base Model Preparation Stage"
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = BaseModelPreparationPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "Model Training Stage"

# try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = ModelTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Model Evaluation Stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e