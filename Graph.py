import os
import sqlite3

def EhPalavraChave(diretorio, arquivo):
    if r'...' in diretorio:
        return True
    if 'PalavraChave' in arquivo.lower():
        return True
    return False

def GetExtensao(arquivo, ListaExtensao):
    for extensao in ListaExtensao:
        if arquivo.endswith(extensao):
            return extensao

def EhExtensao(arquivo, ListaExtensao):
    for extensao in ListaExtensao:
        if arquivo.endswith(extensao):
            return True

def GetListaFontes(pasta, ListaExtensao, con):
    cur = con.cursor()
    PalavraChaveFonteQuantidade = 0
    try:
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:  
                if (EhExtensao(arquivo, ListaExtensao) and EhPalavraChave(diretorio, arquivo)):
                    PalavraChaveFonteQuantidade += 1
                    cur.execute(f'INSERT OR IGNORE INTO ARQUIVOS (ARQUIVO, CAMINHO, EXTENSAO) VALUES ("{arquivo}", "{diretorio}", "{GetExtensao(arquivo, ListaExtensao)}")')
        con.commit()
        print(F'{PalavraChaveFonteQuantidade} arquivos inseridos')
    finally:
        con.close()

def Main():
    print('Aguarde')

    con = sqlite3.connect(r"C:\...\NomeFonte\...explorer.db")
    ListaExtensao = ['.pas', '.dfm', 'inc', '.dproj', '.dpk', '.res', '.dpr']
    pasta = r'd:\...\Fontes'

    GetListaFontes(pasta, ListaExtensao, con)
Main()