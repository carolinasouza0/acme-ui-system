import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Configurações de Diretórios
DOCS_DIR = "./docs"
DB_DIR = "./chroma_db"

def main():
    print("🏗️ Iniciando a construção da memória do Agente (RAG)...")

    # 1. Carregar os documentos Markdown do Design System
    print(f"📄 Lendo arquivos em {DOCS_DIR}...")
    loader = DirectoryLoader(
        DOCS_DIR, 
        glob="**/*.md", 
        loader_cls=TextLoader,
        loader_kwargs={'autodetect_encoding': True}
    )
    documents = loader.load()
    print(f"✅ {len(documents)} documentos carregados.")

    # 2. Fatiar os textos (Chunking)
    # Separamos por blocos lógicos para a IA não perder o foco
    print("✂️ Fatiando os documentos em pedaços otimizados...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", "##", "###", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"✅ Documentos divididos em {len(chunks)} chunks.")

    # 3. Inicializar o modelo de Embedding (100% Open Source e Local)
    # Este modelo transforma texto em vetores sem enviar dados para a internet
    print("🧠 Baixando/Carregando o modelo de embeddings (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Criar e salvar o banco de dados vetorial local (Chroma)
    print(f"💾 Salvando vetores no banco ChromaDB local em {DB_DIR}...")
    
    # Se o banco já existir, vamos recriá-lo para evitar duplicações no ambiente de dev
    if os.path.exists(DB_DIR):
        import shutil
        shutil.rmtree(DB_DIR)

    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_DIR
    )
    
    print("🚀 Sucesso! O conhecimento do Design System foi injetado.")
    print("O Agente agora pode pesquisar os componentes no banco vetorial.")

if __name__ == "__main__":
    main()