from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import ModelTraining
from cnnClassifier import logger

STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training_object = ModelTraining(config=training_config)
        training_object.get_base_model()
        training_object.train_valid_generator()
        training_object.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e