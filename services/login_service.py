import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import EMAIL, PASSWORD

logging.basicConfig(filename='login_errors.log', level=logging.ERROR)

def login(driver):
    try:
        campo_usuario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        campo_usuario.send_keys(EMAIL)

        campo_senha = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        campo_senha.send_keys(PASSWORD)

        formulario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'form'))
        )
        formulario.submit()

        return True

    except Exception as e:
        logging.error("Erro durante o login:", exc_info=True)
        return False
