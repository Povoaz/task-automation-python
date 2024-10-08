#importar bibliotecas
import pyautogui
import time
#pause por comandos
pyautogui.PAUSE = 1
#comandos iniciais para abrir o navegador
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
#link do formulario
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#comando para entrar no site
pyautogui.press("enter")
#dar uma pausa de 3 segundos
#importar o time
time.sleep(3)
#clicar com o mouse agora
#colocar o email
pyautogui.click(x=505, y=404)
pyautogui.write("mariamboja123@gmail.com")
#colocar a senha
pyautogui.click(x=498, y=506)
pyautogui.write("meresuco4321")
#precionar enter
pyautogui.click(x=677, y=566)
pyautogui.press("enter")
time.sleep(2)
#importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
#cadastrar produtos
pyautogui.click(x=605, y=290)

linha = 0
#para cada linha da minha tabela excutar o comando
#INDENTAÇAO = TAB   Hashtag
for linha in tabela.index:
    #texto = string = str
    #selecionar o primeiro campo
    pyautogui.click(x=605, y=290)
    #codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preço unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #observação = nan = not a number = vazio
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    #depois clicar no botão enviar
    pyautogui.press("enter")
    #rolar a tela pra cima dnv
    pyautogui.scroll(1000)








