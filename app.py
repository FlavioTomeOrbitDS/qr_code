from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

dir_path = os.getcwd()

chrome_options2 = Options()
#chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/profile/whatsapp")

# Corrigido: Use 'options' em vez de 'chrome_options'
driver = webdriver.Chrome(options=chrome_options2)

driver.get("https://web.whatsapp.com")
 # Aguarda o QR code aparecer
qr_code_element = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan me!']"))
)

# Captura o HTML do QR code
qr_code_html = qr_code_element.get_attribute('outerHTML')
print("HTML do QR Code:", qr_code_html)


time.sleep(120)
