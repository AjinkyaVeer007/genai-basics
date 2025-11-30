from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

user_query = input("> ")

search_result = vector_store.similarity_search(query=user_query)

CONTEXT = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number:{result.metadata["page_label"]}\nFile Location: {result.metadata["source"]}" for result in search_result])

SYSTEM_PROMPT = f"""
    You are a helpful AI assistant who answers user query based on the available context  retrieved 
    from a pdf file along with page content and page number.

    You should only answer the user based on following context and navigate the user to open the right page
    number to know more.

    Context : 
        {CONTEXT}

"""

client = OpenAI()

res = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content" : SYSTEM_PROMPT}
    ]
)

print(res.choices[0].message.content)