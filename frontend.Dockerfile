# Usa uma imagem leve do Node
FROM node:20-alpine

WORKDIR /app

# Copia os arquivos de dependência
COPY package*.json ./

# Instala as dependências do Next.js
RUN npm install

# Expõe a porta do Next.js
EXPOSE 3000

# Comando para rodar em modo de desenvolvimento (permite hot-reload)
CMD ["npm", "run", "dev"]