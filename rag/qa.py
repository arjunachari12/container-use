
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="/app/chroma", embedding_function=embeddings)

retriever = db.as_retriever()
docs = retriever.get_relevant_documents("What is this document about?")

llm = ChatOpenAI()
response = llm.invoke(docs[0].page_content)

print(response)
