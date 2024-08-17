from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import base64
import os

# Configura o caminho para o ChromeDriver
chrome_driver_path = 'caminho/para/seu/chromedriver'

# Configura as opções do navegador Chrome
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Adiciona o argumento headless
chrome_options.add_argument("--window-size=1920,1080")  # Define o tamanho da janela
#chrome_options.add_argument("--user-data-dir=" + os.path.join(os.getcwd(), "profile", "whatsapp"))
chrome_options.add_argument("--disable-gpu")  # Desativa o GPU
chrome_options.add_argument("--no-sandbox")  # Desativa o modo sandbox para facilitar a execução do script em ambientes seguros
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas no container ao limitar o uso da memória

# Inicializa o driver
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abre o WhatsApp Web
    driver.get("https://web.whatsapp.com")

    # Aguarda o QR code aparecer
    qr_code_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan me!']"))
    )

    # Captura a imagem do QR code
    qr_code_base64 = qr_code_element.screenshot_as_base64
    qr_code_image = Image.open(BytesIO(base64.b64decode(qr_code_base64)))

    # Aqui você pode salvar a imagem ou fazer o que precisar com ela
    qr_code_image.save("QR_Code.png")

finally:
    # Fecha o navegador após a execução
    driver.quit()
