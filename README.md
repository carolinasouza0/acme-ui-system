# 🤖 UI-Gen Architect (Design System AI Agent)

Um Agente de Inteligência Artificial Full-Stack que atua como Arquiteto de Front-end. Ele utiliza **RAG (Retrieval-Augmented Generation)** para ler a documentação do Design System local da empresa e gerar códigos React (Next.js + Tailwind v4 + Shadcn) estritamente dentro dos padrões estabelecidos.

![Arquitetura: Next.js + FastAPI + LangChain + Ollama](https://img.shields.io/badge/Architecture-RAG_Full_Stack-blue)
![Docker](https://img.shields.io/badge/Docker-Conteinerizado-2496ED?logo=docker&logoColor=white)

## 🏗️ Arquitetura do Sistema

O projeto é dividido em microsserviços orquestrados via Docker:
- **Frontend (Porta 3000):** Next.js 16 (Turbopack) com Tailwind CSS v4. Interface limpa para interação com o Agente.
- **Backend API (Porta 8000):** FastAPI em Python. Responsável por orquestrar o LangChain e consultar o banco vetorial.
- **Vector Database:** ChromaDB local contendo os embeddings da documentação do Design System.
- **LLM Engine (Host):** Llama 3.2 (3B) rodando via Ollama diretamente na máquina física para máxima performance.

## 🚀 Como Executar Localmente (Onboarding)

### Pré-requisitos Cruciais
Para que a Inteligência Artificial rode com performance nativa usando sua GPU/CPU, o motor da IA deve rodar **fora** do Docker.
1. Instale o Docker e o Docker Compose.
2. Instale o [Ollama](https://ollama.com/) na sua máquina.
3. Baixe o modelo utilizado pelo projeto rodando no seu terminal:
   ```bash
   ollama pull llama3.2
    ```
### Iniciando o Ambiente
1. Clone o repositório.
2. Inicie o servidor do Ollama permitindo conexões do Docker (mantenha este terminal aberto):
    - Linux/WSL/Mac: `OLLAMA_HOST="0.0.0.0" ollama serve`
    - Windows (PowerShell): `$env:OLLAMA_HOST="0.0.0.0"; ollama serve`
3. Em outro terminal, na raiz do projeto, suba a infraestrutura:
    ```bash
    docker-compose up --build
    ```
4. Acesse `http://localhost:3000` no seu navegador para interagir com o Agente.