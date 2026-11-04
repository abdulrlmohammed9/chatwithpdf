import gradio as gr
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

load_dotenv()

# Global store for the VectorStore to persist between interactions
vector_store = None


def process_pdf(file):
    global vector_store

    if file is not None:
        pdf_reader = PdfReader(file.name)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text)
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        return "PDF Processed. You can now ask questions."
    else:
        return "Please upload a valid PDF."


def ask_question(query):
    global vector_store
    if vector_store is None:
        return "Please upload and process a PDF first."
    if query.strip() == "":
        return "Please enter a question."

    docs = vector_store.similarity_search(query=query, k=3)
    llm = OpenAI()
    chain = load_qa_chain(llm=llm, chain_type="stuff")

    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=query)
        print(cb)

    return response


# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## 📄 Chat With PDF")

    with gr.Row():
        pdf_input = gr.File(label="Upload your PDF", file_types=[".pdf"])
        upload_output = gr.Textbox(label="Status", interactive=False)
        upload_btn = gr.Button("Process PDF")

    question = gr.Textbox(label="Ask Questions to your PDF file")
    answer = gr.Textbox(label="Answer", interactive=False)
    ask_btn = gr.Button("Get Answer")

    upload_btn.click(process_pdf, inputs=pdf_input, outputs=upload_output)
    ask_btn.click(ask_question, inputs=question, outputs=answer)

if __name__ == "__main__":
    demo.launch()