# Passo a passo do projeto
# Código da aula "aprendapython"
# Biblioteca pyautogui para automação com sistema operacional
import pyautogui as py
# Biblioteca time para controlar o tempo de espera
import time

#define uma pausa de 9 segundos entre cada comando
py.PAUSE = 0.9

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl+c, Ctrl+v, Alt Tab...)

# 1. Abrir o sistema da empresa
# https://wfveiculos.com.br/
# Abrir o navagador (chome)
py.press("win")
py.write("chrome")
py.press("enter")

# Entrar no site do sistema
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")

#espera o site carregar em 3 segundos
time.sleep(5)

# 2. Fazer login
py.click(x=197, y=391)
py.write("teste@teste.com")
py.press("tab")
py.write("7kFMpledPXaIXqR")
py.press("enter")

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas (aqui começa o uso do pandas), numpy openpyxl
# Biblioteca pandas para 
import pandas as pd
#tabela recebe a leitura do arquivo produtos
tb = pd.read_csv("produtos.csv")

print(tb)

# 4. Cadastrar um produto
for l in tb.index:
    code = str(tb.loc[l, "codigo"])
    # clicar no campo do código do produto
    py.click(x=264 , y=294)
    # preencher o código 
    py.write(str(tb.loc[l, "codigo"]))
    # passar pro próximo campo
    py.press("tab")
    # marca
    py.write(str(tb.loc[l, "marca"]))
    # passar pro próximo campo
    py.press("tab")
    # tipo
    py.write(str(tb.loc[l, "tipo"]))
    # passar pro próximo campo
    py.press("tab")
    # categoria
    py.write(str(tb.loc[l, "categoria"]))
    # passar pro próximo campo
    py.press("tab")
    # preço
    py.write(str(tb.loc[l, "preco_unitario"]))
    # passar pro próximo campo
    py.press("tab")
    # custo
    py.write(str(tb.loc[l, "custo"]))
    # passar pro próximo campo
    py.press("tab")
    # obs
    obs = str(tb.loc[l, "obs"]))
    if obs != "nan":
            py.write(obs)
    # passar pro próximo campo
    py.press("tab")
    # enter de cadastrar o produto
    py.press("enter")
    py.scroll(6000)

# 5. Repetir isso tudo até acabar a lista de produtos

