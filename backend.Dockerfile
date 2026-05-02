# Usa uma imagem leve do Python
FROM python:3.10-slim

WORKDIR /app

# Instala ferramentas do sistema necessárias para compilar algumas bibliotecas
RUN apt-get update && apt-get install -y build-essential

# Copia e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da API
COPY api.py .

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]