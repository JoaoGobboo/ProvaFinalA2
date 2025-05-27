# Dockerfile para API de Pagamentos (PHP)
FROM php:8.1-cli

# Instalar curl para healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar código da aplicação
COPY index.php .

# Expor porta
EXPOSE 3003

# Comando para executar a aplicação
CMD ["php", "-S", "0.0.0.0:3003"]