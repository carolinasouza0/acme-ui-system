from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
import os
import warnings

warnings.filterwarnings("ignore")

app = FastAPI(title="UI-Gen Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

OLLAMA_BASE_URL = os.getenv("OLLAMA_URL", "http://ollama.local:11434")

# 1. Carrega as Inteligências
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3})
llm = ChatOllama(model="llama3.2", temperature=0, base_url=OLLAMA_BASE_URL)

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        # 2. NÓS fazemos a busca da documentação (Tiramos essa responsabilidade da IA)
        docs = retriever.invoke(req.message)
        contexto_design_system = "\n\n".join([doc.page_content for doc in docs])

        # 3. Montamos o Super Prompt já com a resposta mastigada para a IA
        prompt_final = f"""Você é um Arquiteto de Front-end Sênior.
Sua única tarefa é gerar código React usando APENAS os componentes documentados abaixo.

CONTEXTO DO DESIGN SYSTEM (Use estritamente estas propriedades):
{contexto_design_system}

REGRAS ABSOLUTAS:
1. NUNCA invente propriedades que não estão no contexto acima.
2. Retorne APENAS o código funcional dentro de blocos ```tsx
3. Use Tailwind CSS para layout (ex: flex, gap-4).
4. Não adicione textos explicativos, apenas o bloco de código.

PEDIDO DO USUÁRIO: {req.message}"""

        # 4. Chamada direta (Rápida e sem alucinações)
        response = llm.invoke([HumanMessage(content=prompt_final)])
        
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}