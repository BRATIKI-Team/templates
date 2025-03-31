import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

class ChromaService:
    def __init__(self):
        self.__db = chromadb.PersistentClient(path="./chroma_db")
    
    def get_or_create_vector_store(self, collection_name: str) -> ChromaVectorStore:
        collection = self._get_or_create_collection(collection_name)
        print(f"fond collection by name {collection_name}", collection)

        return ChromaVectorStore(collection)
    
    def drop_collection_if_exists(self, collection_name: str) -> None:
        try:
            self.__db.delete_collection(collection_name)
        except Exception as e:
            print(f"Error dropping collection {collection_name}: {e}")

    def _get_or_create_collection(self, name: str) -> chromadb.Collection:
        return self.__db.get_or_create_collection(name)