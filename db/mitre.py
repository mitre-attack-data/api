from typing import List
from settings.configurations import DefaultConfig
from db import DataBase


config = DefaultConfig()


class DataBaseMitre(DataBase):

    def __init__(self, collection='mitre_data') -> None:
        super().__init__(data_base=config.DATABASE_NAME_MITRE, collection=collection)
        self.collection = collection
        
    
    def list_tactics(self) -> List[dict]:
        tactics_list = self.client[self.data_base][self.collection].find({}, {"_id": 0})
        tactics_list = [i for i in tactics_list]
        return tactics_list

    # def get_user(self, username):
    #     users_list = self.client[self.data_base][self.collection].find()
    #     user_data = [user for user in users_list if user['username'] == username]
        
    #     if user_data:
    #         user_data = user_data.pop()
    #         user_data.update({"username": username})
    #         return UserInDB(**user_data)
        
    #     return None

    def list_techniques_by_tactic(self, tactic_shortname: str) -> List[dict]:
        pass
  
    def insert_many(self, data: List[dict]):
        try: 
            _ = self.client[self.data_base][self.collection].insert_many(data)
        
        except Exception as error:
            print(f"Error on insert_many DataBaseMitre. Error message: {error}")
            return False

        else:
            return True
