from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager # Faz Download automatico do Driver Correto
from selenium.webdriver.common.by import By # Permite Localizar os elementos por ID, Classe ou Xpath
import time

# Estrutura
# Configuração Automática: O Service vai baixar o driver compatível sozinho

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#DEFINE um tempo de espera padrão (se a internet estiver lenta, aguarde 10s)

navegador.implicitly_wait(10)

print("Acessando um site alvo")
navegador.get("https://g1.globo.com/")
time.sleep(10)
input("Digite s para sair")

print("Buscando o Alvo no site ...")

# logo = navegador.find_element(By.XPATH,"/html/body/header/div/div/div/a")

endereco = "/html/body"
livro = navegador.find_element(By.XPATH,endereco)


print("O Texto extraido foi: ",livro)