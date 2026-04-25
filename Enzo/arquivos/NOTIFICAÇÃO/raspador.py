from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configuração automática do driver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Tempo de espera implícito
navegador.implicitly_wait(10)

print("Acessando um site alvo")

navegador.get("https://youtube.com.br")
time.sleep(60)