# Web Scraping

from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import pyodbc


options = Options()
options.add_argument('window-size=400, 800')
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)

navegador.get('http://127.0.0.1:5500/Index.html')
sleep(2)

while True:
    page_content = navegador.page_source

    site = BeautifulSoup(page_content, 'html.parser')

    cond = site.find("table", class_='cont_seg')

    tabela = pd.DataFrame(cond)
    print(tabela)
    


# SQL Server

    dados_conexao = (
        "Driver={SQL Server};"
        "Server=localhost;"
        "Database=PythonSQL;"
    )

    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")

    cursor = conexao.cursor()

    comando = f"""INSERT INTO niveis(Nível)
    VALUES
        ('{cond}')"""
    
    cursor.execute(comando)
    cursor.commit()  

    sleep(1)