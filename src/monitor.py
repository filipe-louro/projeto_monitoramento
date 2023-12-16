from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_service import login

driver = webdriver.Chrome()

url = 'https://www.pichau.com.br/'

driver.get(url)

try:
    login(driver)
    produto_desejado = "Nome do Produto"
    # Espera até que o elemento do produto desejado seja carregado na página
    elemento_produto = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(text(), '{produto_desejado}')]"))
    )

    # Obter o preço do produto
    preco_produto = elemento_produto.find_element(
        By.XPATH, '../../div/div[@class="price-new"]').text
    # Aqui você pode comparar o preço com o valor desejado e tomar a ação adequada

    # Exemplo de ação: clicar no produto
    elemento_produto.click()

    # Aqui você pode adicionar código para fazer o checkout e preencher os detalhes necessários

except Exception as e:
    print("Erro ao localizar o produto:", e)
finally:
    # Fecha o navegador
    driver.quit()
