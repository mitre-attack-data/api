from settings.configurations import DefaultConfig
from schemas.auth import UserSignUp
from schemas.user import UserInDB
from db.database import DataBase


config = DefaultConfig()


class DataBaseUser(DataBase):

    def __init__(self, collection='users_data') -> None:
        super().__init__(data_base=config.DATABASE_NAME_USERS, collection=collection)
        self.users_collection = collection

    
    def get_user(self, username):
        users_list = self.client[self.data_base][self.users_collection].find()
        user_data = [user for user in users_list if user['username'] == username]
        
        if user_data:
            user_data = user_data.pop()
            user_data.update({"username": username})
            return UserInDB(**user_data)
        
        return None
    
    
    def get_user_by_email(self, email):
        users_list = self.client[self.data_base][self.users_collection].find()
        user_data = [user for user in users_list if user['email'] == email]
        
        if user_data:
            user_data = user_data.pop()
            return UserInDB(**user_data)
        
        return None

  
    def insert_one(self, user_data: UserSignUp):
        try: 
            data = user_data.dict()
            del data['password']
            _ = self.client[self.data_base][self.users_collection].insert_one(data)
        
        except Exception as error:
            print(f"Error on insert_one DataBase. Error message: {error}")
            return False

        else:
            return True

    
    def update_one(self, user_data: UserInDB):
        finded_user_data = self.get_user(user_data.username)
        
        if not finded_user_data:
            return False

        # Remove null values from dict
        new_data ={k: v for k, v in user_data.dict().items() if v}

        db_query    = {"username": user_data.username }
        db_new_data = {"$set": new_data}
        
        ans = self.client[self.data_base][self.users_collection].update_one(
            filter=db_query,
            update=db_new_data
        )

        # print(ans.raw_result)
        return True
