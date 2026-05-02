# Changelog
Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.
O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

## [1.0.0] - 2026-05-02
### Adicionado
- Interface web (Front-end) desenvolvida em Next.js para interação amigável com a IA.
- Backend em FastAPI configurado para atuar como ponte entre o Front-end e o LangChain.
- Arquitetura RAG Direto (Retrieval-Augmented Generation) implementada para garantir que o LLM não gere "alucinações" fora do Design System.
- Containerização completa (Docker Compose) separando Front-end e API em ambientes isolados e escaláveis.
- Estilização corporativa e Modo Escuro utilizando Tailwind CSS v4 e Shadcn UI.
- Banco de dados vetorial ChromaDB persistido via volumes do Docker.

### Corrigido
- `Hydration Error` no React causado por injeção de extensões do navegador através do uso de `suppressHydrationWarning`.
- Conflito de compilação do Tailwind v4 no Docker usando mapeamento absoluto de volumes na raiz do projeto.
- Bypass de validação de rede IPv6 do Pydantic utilizando injeção de DNS customizado (`ollama.local`) no `docker-compose.yml`.
- Falha de conexão entre Docker e Host (Ollama Connection Refused) através da abertura dinâmica da porta (`0.0.0.0`).
- Substituição da arquitetura de "Agent Router" por "RAG Direto" para evitar retornos em formato JSON quebrado em modelos menores (Llama 3.2 3B).

### Melhorias Futuras
1. Streaming de Resposta para feedback em tempo real.
   - O problema atual: O usuário clica em "Gerar" e fica esperando 15 segundos olhando para um botão bloqueado até a resposta inteira aparecer de uma vez.
   - A melhoria: Implementar "Server-Sent Events (SSE)" no FastAPI e no React. Isso faz com que a IA digite o código na tela do usuário palavra por palavra (efeito máquina de escrever), exatamente como o ChatGPT faz. A sensação de velocidade melhora muito, mesmo que o tempo total seja o mesmo.
2. Live Preview Interativo (O "Efeito Vercel v0"):
    - A melhoria: Em vez de apenas exibir o código fonte, criar uma aba "Preview" do lado direito usando a biblioteca react-live ou renderização segura em Iframe. A IA gera o código e você já vê o formulário/card renderizado e clicável na tela!
3. Expansão do Banco RAG:
    - A melhoria: Hoje o banco vetorial tem apenas Botões, Cards e Inputs. O ideal é expandir para todos os componentes do Design System (Dropdowns, Modais, Tabelas, etc) e também incluir exemplos de uso, variações de estilo e até mesmo casos de uso comuns. Quanto mais rico for o banco RAG, mais precisa e útil será a geração de código da IA.
4. Cache Semântico (Velocidade):
    - O problema atual: Cada vez que o usuário pede para gerar um componente, a IA precisa consultar o banco vetorial, o que pode levar alguns segundos.
    - A melhoria: Implementar um cache semântico em memória (usando LRU Cache ou Redis) para armazenar as consultas mais frequentes. Assim, se um usuário pedir para gerar um "Card" e outro usuário pedir o mesmo "Card" logo depois, a resposta pode ser instantânea sem precisar consultar o banco vetorial novamente.
