from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://www.hashtagtreinamentos.com/")
navegador.maximize_window()
barra_youtube = navegador.find_element("name", "Quero aprender") 

time.sleep(30)




