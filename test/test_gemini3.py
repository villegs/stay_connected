
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import config
from langchain.document_loaders import DirectoryLoader
import PyPDF2
from langchain.chains import RetrievalQA
# from langchain.vectorstores import FAISS
import faiss
from langchain.chains.retrieval import create_retrieval_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
# Replace 'your_api_key' with your actual Google GenAI API key
os.environ["GOOGLE_API_KEY"] = config.gemini_api_key


class FAISSRetriever:
    def __init__(self, index, documents, model):
        self.index = index
        self.documents = documents
        self.model = model

    def retrieve(self, query, k=1):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding, dtype=np.float32), k)
        results = [self.documents[i] for i in indices[0]]
        return results


def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

if __name__ == '__main__':
    # Path to your PDF file
    # pdf_path = 'path_to_your_pdf_file.pdf'

    # Extract text from PDF
    # pdf_text = extract_text_from_pdf(pdf_path)
    # Load documents from the directory

    directory_path = "../documents/test"
    loader = DirectoryLoader(directory_path, glob="*.pdf")
    documents = loader.load()

    # Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(documents)
    chunks = [doc.page_content for doc in documents]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype=np.float32))
    retriever = FAISSRetriever(index, documents, model)

    # Initialize the vector store
    # vector_store = FAISS.from_texts(chunks, embeddings)

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    retrieval_chain = create_retrieval_chain(
        retriever=retriever,
        llm=llm
    )

    # Questions to ask
    questions = [
        "What is the main topic of the document?",
        "Can you summarize the key points?",
        "What are the conclusions or recommendations?"
    ]
    for question in questions:
        answer = retrieval_chain.run(question)
        print(f"Q: {question}\nA: {answer['result']}\n")