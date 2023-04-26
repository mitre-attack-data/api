import pymongo

from pymongo import errors
from settings.configurations import DefaultConfig



config = DefaultConfig()


class DataBase:
    """
    Only an IP address you add to your Access List will be able to 
    connect to your project's clusters. You can manage existing IP 
    entries via the Network Access Page.
    """

    def __init__(self, data_base: str, collection: str) -> None:
        self.users_collection = collection
        self.data_base = data_base
        self.client = None
        
        try:
            CONNECTION_DB = f"mongodb+srv://{config.CLUSTER_USERNAME}:{config.CLUSTER_PASSWORD}@cluster0.4hm7suw.mongodb.net/{data_base}?retryWrites=true&w=majority"
            self.client = pymongo.MongoClient(CONNECTION_DB)
        
        except errors.ConnectionFailure:
            raise errors.ConnectionFailure(
                message='Error connect to MongoDB'
            )    
