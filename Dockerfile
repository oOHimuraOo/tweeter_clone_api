# Usando a imagem oficial do Python 3.12
FROM python:3.12-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Instalando as dependências com pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiando todo o código para o contêiner
COPY . /app/

# Expondo a porta do Django
EXPOSE 8000

# Comando para rodar o Django no contêiner
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
