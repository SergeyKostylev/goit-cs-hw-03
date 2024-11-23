from pymongo import MongoClient


class Connection():
    def __init__(self):
        self.__client = MongoClient('mongodb://localhost:27017/')
        db = self.__client['animals']
        self.__collection = db['cats']

    def get_collection(self):
        return self.__collection

    def fill_cats(self):
        documents = [
            {
                "name": "Masik",
                "age": 3,
                "features": ["cozy", "red"]
            },
            {
                "name": "Mot",
                "age": 9,
                "features": ["angry", "fat", "grey"]
            },
            {
                "name": "Bom",
                "age": 7,
                "features": ["angry", "fat", "grey"]
            }
        ]

        for document in documents:
            self.get_collection().insert_one(document)


if __name__ == '__main__':
    client = Connection()
    client.fill_cats()
