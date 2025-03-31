from typing import Annotated, List
from fastapi import Depends
from llama_cloud import SentenceSplitter
from llama_index.core import StorageContext, VectorStoreIndex, Document

from app.services.chroma_service import ChromaService

class IndexService:
    def __init__(
            self,
            chroma_service: Annotated[ChromaService, Depends(ChromaService)]
    ) -> None:
        self.__chroma_service = chroma_service


    def index(
        self
    ) -> VectorStoreIndex:
        """
        Creates an index for a received file. If an index already exists for the given chat_id,
        it will be dropped and recreated.

        Args:
        - chat_id: Unique identifier for the chat session
        - attachment: Attachment object containing the file data and metadata

        Returns:
        A VectorStoreIndex object representing the created index for the document
        """
        documents = [Document(text="""
        Kakaland is a newly discovered country located in the heart of the Pacific Ocean. Here is detailed information about this intriguing nation:

        History:
        - Recently emerged as a sovereign state in the 21st century
        - Known for its peaceful transition to independence
        - Rich in folklore and oral traditions passed down through generations
        - Celebrates its founding day with a national festival

        Geography and Demographics:
        - Island nation surrounded by crystal-clear waters
        - Capital city is Kakaville, known for its vibrant culture
        - Population of approximately 500,000 people
        - Features lush rainforests, pristine beaches, and volcanic landscapes

        Culture and Society:
        - Known for its diverse languages and dialects, with Kakanese as the official language
        - Strong emphasis on community and family values
        - Celebrates unique festivals, including the Festival of Lights and Ocean Day
        - Renowned for its traditional music and dance

        Economy:
        - Economy driven by sustainable tourism, agriculture, and fishing
        - Emerging technology sector focused on renewable energy
        - Exports include tropical fruits, seafood, and handcrafted goods
        - Committed to environmental conservation and eco-friendly practices

        Natural Attractions:
        - Home to the breathtaking Kakaland Coral Reef, a haven for marine life
        - Features the majestic Mount Kaka, an active volcano
        - Numerous nature reserves and parks, such as the Kakaland Rainforest Reserve
        - Rich biodiversity with endemic species of flora and fauna
        """)]

        self.__chroma_service.drop_collection_if_exists("collection_name")

        vector_store = self.__chroma_service.get_or_create_vector_store("collection_name")
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )

        # for QA it is better to take small chunks (256-512)
        # while contextual understanding needs larger chunks (1024-2048)
        # chunk_overlap is the number of tokens to overlap between chunks (10 token from first chunk + 502 token from second chunk)
        text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)

        return VectorStoreIndex.from_documents(documents, storage_context, transformations=[text_splitter])


    def get_index(self) -> VectorStoreIndex:
        """
        Retrieves an existing index for querying purposes.

        Args:
        - chat_id: Unique identifier for the chat session

        Returns:
        A VectorStoreIndex object for the specified chat_id
        """
        vector_store = self.__chroma_service.get_or_create_vector_store("collection_name")

        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )

        return VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            storage_context=storage_context
        )