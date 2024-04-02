#####################################################################################################
# from selenium import webdriver


# https://selenium-python.readthedocs.io/index.html
# driver = webdriver.Chrome()
# driver.get('https://www.linkedin.com/')

#####################################################################################################


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Acho que é para definir que usaremos o chrome        ######################### OLHAR ISSO COM ATENÇÃO #########################
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# Iniciando uma instância do Chrome WebDriver verifica e baixa o webdriver correspondente 
servico = Service(ChromeDriverManager().install())

# Indica que é para utilizar o webdriver que foi salvo na variável servico
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Definindo o site que terá os dados extraídos  
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
url = 'https://www.linkedin.com/company/94807383/admin/analytics/updates/'
navegador.get(url)
 
# Colocando login e senha no linkedin (há dois modos exemplificados)
navegador.find_element('xpath', '//*[@id="username"]').send_keys(login)
navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
navegador.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button').click()

# Acessando as Análises
#


