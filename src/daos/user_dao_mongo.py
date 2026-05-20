import os
from dotenv import load_dotenv
from pymongo import MongoClient  
from models.user import User


class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)
            db_host = os.getenv("MONGODB_HOST")
            db_port = int(os.getenv("MONGODB_PORT", 27017))
            db_name = os.getenv("MONGODB_DB_NAME")
            db_user = os.getenv("MONGODB_USERNAME")
            db_pass = os.getenv("MONGODB_PASSWORD")
            self.client = MongoClient(
                host=db_host,
                port=db_port,
                username=db_user,
                password=db_pass,
                authSource="admin",
                serverSelectionTimeoutMS=5000,
            )
            self.client.admin.command("ping")
            self.db = self.client[db_name]
            self.collection = self.db["users"]
            self._seed_users()
        except FileNotFoundError as e:
            raise RuntimeError("Attention : Veuillez créer un fichier .env") from e
        except Exception as e:
            raise RuntimeError("Impossible de se connecter à MongoDB : " + str(e)) from e

    def _seed_users(self):
        if self.collection.count_documents({}) == 0:
            self.collection.insert_many([
                {"name": "Ada Lovelace", "email": "alovelace@example.com"},
                {"name": "Adele Goldberg", "email": "agoldberg@example.com"},
                {"name": "Alan Turing", "email": "aturing@example.com"},
            ])

    def select_all(self):
        """ Select all users from MongoDB """
        documents = self.collection.find()
        return [User(document["_id"], document["name"], document["email"]) for document in documents]

    def insert(self, user):
        """ Insert given user into MongoDB """
        result = self.collection.insert_one({"name": user.name, "email": user.email})
        return result.inserted_id

    def update(self, user):
        """ Update given user in MongoDB """
        self.collection.update_one(
            {"_id": user.id},
            {"$set": {"name": user.name, "email": user.email}},
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.collection.delete_one({"_id": user_id})

    def close(self):
        self.client.close()
