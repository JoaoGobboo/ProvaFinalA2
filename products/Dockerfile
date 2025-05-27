# Dockerfile para API de Produtos (Node.js)
FROM node:18-alpine

# Instalar curl para healthcheck
RUN apk add --no-cache curl

# Definir diretório de trabalho
WORKDIR /app

# Criar package.json
RUN echo '{ \
  "name": "products-api", \
  "version": "1.0.0", \
  "description": "API de Produtos", \
  "main": "index.js", \
  "scripts": { \
    "start": "node index.js" \
  }, \
  "dependencies": { \
    "express": "^4.18.2" \
  } \
}' > package.json

# Instalar dependências
RUN npm install

# Copiar código da aplicação
COPY index.js .

# Expor porta
EXPOSE 3001

# Comando para executar a aplicação
CMD ["npm", "start"]