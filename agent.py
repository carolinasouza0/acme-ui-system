from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.tools import create_retriever_tool
from langchain_core.messages import SystemMessage, HumanMessage # NOVOS IMPORTS
from langgraph.prebuilt import create_react_agent
import warnings

# Ignora warnings visuais menos importantes
warnings.filterwarnings("ignore")

def main():
    print("⚙️ Iniciando o Cérebro do Agente (LangGraph - Método Bulletproof)...")

    # 1. Reconectar ao Banco Vetorial Local
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})

    # 2. Definir a Ferramenta (Tool)
    tool = create_retriever_tool(
        retriever,
        "buscar_documentacao_ds",
        "Pesquisa a documentação oficial do Design System da empresa. Use esta ferramenta ANTES de gerar qualquer código para saber quais componentes existem."
    )
    tools = [tool]

    # 3. Configurar o LLM Local (Llama 3.2 leve)
    llm = ChatOllama(model="llama3.2", temperature=0)

    # 4. Instanciar o Agente Moderno (Limpo, sem parâmetros de modificador)
    agent_executor = create_react_agent(llm, tools)

    # 5. Prompt de Sistema (Os Guardrails) - Será injetado na chamada
    system_prompt = """Você é o "UI-Gen Agent", um Arquiteto de Front-end Sênior.
    Sua tarefa é criar componentes React usando APENAS o Design System local da empresa.
    
    REGRAS CRÍTICAS:
    1. Você DEVE usar a ferramenta `buscar_documentacao_ds` para ver como usar os componentes (Button, Card, Input, etc).
    2. Nunca crie componentes do zero se eles existirem na documentação.
    3. Use Tailwind CSS apenas para layout (ex: flex, grid, gap-4, p-4, w-full).
    4. Se precisar de ícones, NUNCA gere SVG. Importe do pacote `lucide-react`.
    5. Retorne APENAS o código funcional dentro de blocos ```tsx e uma justificativa curtíssima das decisões."""

    print("\n" + "="*50)
    print("🤖 UI-Gen Agent online! (Powered by LangGraph)")
    print("Tente pedir: 'Crie um formulário de login com email e senha dentro de um card'")
    print("Digite 'sair' para encerrar.")
    print("="*50 + "\n")

    # 6. Loop de interação (Chat)
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("Desligando agente...")
            break
        
        if not user_input.strip():
            continue

        try:
            # INJEÇÃO À PROVA DE FALHAS:
            # Passamos o SystemMessage (regras) e o HumanMessage (pergunta) juntos a cada turno.
            response = agent_executor.invoke({
                "messages": [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=user_input)
                ]
            })
            
            # A última mensagem na lista sempre é a resposta final da IA
            final_message = response["messages"][-1].content
            
            print("\n" + "="*20 + " RESPOSTA FINAL " + "="*20)
            print(final_message)
            print("="*56 + "\n")
        except Exception as e:
            print(f"\n⚠️ Ocorreu um erro no processamento: {e}")

if __name__ == "__main__":
    main()