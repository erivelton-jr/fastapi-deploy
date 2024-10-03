# Base image
FROM python:3.12.6-alpine3.20

# Instalar dependências necessárias no sistema operacional
RUN apk add --no-cache gcc musl-dev libpq-dev

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivo de dependências para o container
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação para o container
COPY . .

# Expor a porta onde a aplicação será executada
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]