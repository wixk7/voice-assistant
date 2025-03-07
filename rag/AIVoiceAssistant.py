import os
from qdrant_client import QdrantClient
from llama_index.llms.ollama import Ollama
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

import warnings
warnings.filterwarnings("ignore")

class AIVoiceAssistant:
    def __init__(self):
        self._qdrant_url = "http://localhost:6333"
        self._data_path = r"C:\Sathwik\Projects\voice_assistant_llm-main\rag\restaurant_file.txt"
        
        # Initialize Qdrant client
        self._client = QdrantClient(url=self._qdrant_url, prefer_grpc=False)

        # Initialize Ollama LLM with the 'mistral' model
        self._llm = Ollama(model="mistral", request_timeout=120.0)

        # Use a proper embedding model
        Settings.llm = self._llm
        Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

        self._index = None  # Initialize index
        self._create_kb()   # ✅ Creates knowledgebase only if file exists
        self._create_chat_engine()  # ✅ Proceeds only if _index is initialized

    def _create_chat_engine(self):
        if self._index is None:
            print("⚠️ Chat Engine cannot be created as Index is None.")
            return
        
        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        self._chat_engine = self._index.as_chat_engine(
            chat_mode="context",
            memory=memory,
            system_prompt=self._prompt,
        )

    def _create_kb(self):
        try:
            if not os.path.exists(self._data_path):
                print(f"❌ Error: File {self._data_path} does not exist.")
                return  # Exit function if file is missing

            reader = SimpleDirectoryReader(input_files=[self._data_path])
            documents = reader.load_data()

            # Initialize Qdrant Vector Store
            vector_store = QdrantVectorStore(client=self._client, collection_name="kitchen_db")
            storage_context = StorageContext.from_defaults(vector_store=vector_store)

            # Create vector index
            self._index = VectorStoreIndex.from_documents(
                documents, storage_context=storage_context
            )
            print("✅ Knowledgebase created successfully!")
        except Exception as e:
            print(f"❌ Error while creating knowledgebase: {e}")

    def interact_with_llm(self, customer_query):
        if self._chat_engine is None:
            return "⚠️ Chat Engine is not available. Please check the knowledge base setup."

        AgentChatResponse = self._chat_engine.chat(customer_query)
        return AgentChatResponse.response

    @property
    def _prompt(self):
        return """
            You are a professional AI Assistant receptionist working in Bangalore's one of the best restaurants called Bangalore Kitchen.
            Ask the questions mentioned inside square brackets one at a time to keep the conversation engaging!
            
            [Ask for Name and contact number, then what they want to order, and end the conversation with greetings!]

            If you don't know the answer, just say you don't know. Do not make up an answer.
            Provide concise and short answers (not more than 10 words), and don't chat with yourself!
            """
