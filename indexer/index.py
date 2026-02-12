
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("/app/docs/sample.pdf")
docs = loader.load()

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="/app/chroma"
)

db.persist()
print("Indexing complete.")
