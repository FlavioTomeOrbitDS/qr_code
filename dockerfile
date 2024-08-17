# Usa uma imagem oficial do Python com o Debian como base
FROM python:3.8-slim

# Instala dependências necessárias para o Selenium e Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libgconf-2-4 \
    libnss3-dev \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    libindicator7 \
    xdg-utils \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY . /app

# Instala as bibliotecas Python necessárias
RUN pip install selenium Pillow

# Baixa o ChromeDriver e o Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
RUN wget https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip && mv chromedriver /usr/local/bin/chromedriver && chmod +x /usr/local/bin/chromedriver

# Expõe a porta 8080 (opcional)
EXPOSE 8080

# Define o comando para executar o script
CMD ["python", "qrcode_generator.py"]
