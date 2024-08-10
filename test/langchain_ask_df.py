
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import config
from langchain.document_loaders import DataFrameLoader
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from utils.load_and_join_df import retrieve_formatted_df
os.environ["GOOGLE_API_KEY"] = config.gemini_api_key
if __name__ == '__main__':

    df = retrieve_formatted_df(file_path='..')
    loader = DataFrameLoader(df)
    documents = loader.load()

    embedding = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(documents=documents, embedding=embedding)
    retriever = vectorstore.as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
    )

    # Questions to ask
    questions = [
        "Has there been any noticeable trends over time?",
        "How has time to get served evolved over time?",
        "Is there a Center that needs help?"
    ]
    for question in questions:
        result = qa_chain({"question": question})
        print("Answer:", result["answer"])
        print("Sources:", result["sources"])