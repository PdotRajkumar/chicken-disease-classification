from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import Data_ingestion_training_pipeline

logger.info("test log")


STAGE = "Data ingestion stage"
try:
    logger.info(f"stage name:{STAGE} - Started")
    pipeline = Data_ingestion_training_pipeline()
    pipeline.main()
    logger.info(f"stage:{STAGE} - Completed")
except Exception as e:
        logger.exception(e)
        raise e
        