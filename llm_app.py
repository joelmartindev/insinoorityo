from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.documents import Document


PROMPT_TEMPLATE = """
Answer the question based only on the following excerpts from a user submitted PDF:

{context}

---

Answer the question based on the above context in great length: {question}
"""


def process_file(pdf_filepath):

    # Load PDF document into the app
    loader = PyPDFLoader(pdf_filepath)
    docs = loader.load()

    # Split document into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
    chunks = text_splitter.split_documents(docs)

    return chunks


def retrieve(chunks: list[Document], query_text: str):
    # Add chunks to a vector store
    embeddings = FastEmbedEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)

    # Search the vector store for chunks most similar to given query
    results = vector_store.similarity_search(query_text, k=5)

    # Go through results of the search, noting down used sources (pages of the document) and forming a prompt for the LLM
    sources = [doc.metadata.get("page_label", None) for doc in results]
    context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    return prompt, sources


def generate(prompt: str, sources: str):
    # Send the formed prompt to the chosen LLM being run in Ollama
    model = OllamaLLM(model="llama3.1")
    response_text = model.invoke(prompt)

    final_response = f"{response_text}\nSources: {sources}"
    return final_response


def main(pdf_filepath, question):
    chunks = process_file(pdf_filepath)
    prompt, sources = retrieve(chunks, question)
    response = generate(prompt, sources)
    return response


if __name__ == "__main__":
    main()
