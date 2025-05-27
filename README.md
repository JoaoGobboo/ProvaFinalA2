# Explicação dos Arquivos Docker e Docker Compose

## Dockerfiles

Cada pasta tem um dockerfile para sua respectiva API. Segue uma pequena explicação sobre o que cada dockerfile faz por API:

- **Products API**
    - instala o Node.js
    - Copia os arquivos da aplicação
    - instala dependencias do projeto
    -  Execulta o comando para iniciar a API

- **Orders API**
    - define uma imagem base do Python
    - Copia os arquivos da aplicação flask
    - instala dependencias do projeto
    - Execulta o comando para iniciar a API

- **Payments API**
    - define uma imagem base do PHP
    - Copiar código da aplicação
    - define o servidor embutido do PHP para rodar a aplicação

## docker-compose.yml

O docker compose gerencia e configura todos os containers que compõem o sistema. Segue a explicação do arquivo:

- OBS 1: Todas as APIS fazem parte da rede `ecommerce-network` para comunicação interna.
- OBS 2:  Todas as APIS Possuem um healthcheck que verifica os endpoints

- **Products**
    - Cria a imagem Docker a partir do Dockerfile na pasta `./products`.
    - Expõe a porta 3001 para acesso externo.

- **orders**
    - Cria a imagem a partir do Dockerfile na pasta `./orders`.
    - Expõe a porta 3002.
    - Depende dos serviços de banco de dados SQL, redis e products API para iniciar somente após eles estarem disponíveis.
    - Define ambiente para configurar a conexão com o banco de dados e o Redis.

- **payments**
    - Cria a imagem com base no Dockerfile em `./payments`.
    - Expõe a porta 3003.
    - Depende da orders API para iniciar após ele estar disponível.

- **Banco de Dados MySQL**
    - Utiliza a imagem oficial do MySQL 8.0.
    - Define user e senha root e cria o banco ecommerce.
    - Expõe a porta 3307 para acesso externo.
    - Usa volume persistente **mysql_data** para manter os dados mesmo que o container seja reiniciado.

- **redis**
    - Utiliza a imagem oficial do Redis versão 7 em Alpine (imagem leve).
    - Expõe a porta 6379.
