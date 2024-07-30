import os
from langchain_google_genai import ChatGoogleGenerativeAI
import config
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Replace with your actual API key
os.environ["GOOGLE_API_KEY"] = config.gemini_api_key

# Replace with the directory containing your .pds files
directory_path = "../documents/test"

# Load documents from the directory
loader = DirectoryLoader(directory_path, glob="*.pdf")
documents = loader.load()

# Split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Create an embedding model
embeddings = OpenAIEmbeddings()

# Create a vector store
vectorstore = FAISS.from_documents(texts, embeddings)

# Initialize the Gemini model
llm = llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Create a retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
)

# Ask your question
query = "Make a summary about the pdf files."

# Get the response
result = qa_chain.run(query)

print(result)