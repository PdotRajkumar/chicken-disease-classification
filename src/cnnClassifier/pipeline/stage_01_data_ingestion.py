from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

class Data_ingestion_training_pipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()   
        
        
if __name__=="__main__":
    try:
        Logger.info(f"stage:{STAGE} - Started")
        pipeline = Data_ingestion_training_pipeline()
        pipeline.main()
        Logger.info(f"stage:{STAGE} - Completed")
    except Exception as e:
            Logger.exception(e)
            raise e
            
    
    