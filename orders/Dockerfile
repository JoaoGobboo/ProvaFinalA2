# Dockerfile para API de Pedidos (Python)
FROM python:3.11-slim

# Instalar curl para healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências Python
RUN pip install flask redis requests mysql-connector-python

# Copiar código da aplicação
COPY app.py .

# Expor porta
EXPOSE 3002

# Comando para executar a aplicação
CMD ["python", "app.py"]