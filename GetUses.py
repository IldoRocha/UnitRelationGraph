from code import interact
from dataclasses import replace
import sqlite3

def GetUsesInterface(arquivo):
    with open(arquivo, 'r', encoding='ANSI') as buffer:
        string = buffer.read()
        interface = string.split('interface', 1)[1]
        if not 'uses' in interface:
            return []
        interface = interface.split('uses', 1)[1]
        interface = interface.split(';', 1)[0] 
        interface = interface.replace('\n', '')
        interface = interface.replace(' ', '')
        return interface.split(',') 

def GetUsesImplementation(arquivo):
    with open(arquivo, 'r', encoding='ANSI') as buffer:
        string = buffer.read()
        interface = string.split('implementation', 1)[1]
        if not 'uses' in interface:
            return []
        interface = interface.split('uses', 1)[1]
        interface = interface.split(';', 1)[0] 
        interface = interface.replace('\n', '')
        interface = interface.replace(' ', '')
        return interface.split(',') 

def GetUses(arquivo):
    return GetUsesInterface(arquivo), GetUsesImplementation(arquivo)

def SalvarFontes(con, codigo, Interface, Implementation):
    con = sqlite3.connect(r"C:\...\NomeFonte\...explorer.db")
    cur = con.cursor()

    for arquivo in Interface:
        if not arquivo is None:
            cur.execute(f'INSERT OR IGNORE INTO dependencias (arquivo, UsesInterface) VALUES ("{codigo}", "{arquivo}")')

    for arquivo in Implementation:
        if not arquivo is None:
            cur.execute(f'INSERT OR IGNORE INTO dependencias (arquivo, UsesImplementation) VALUES ("{codigo}", "{arquivo}")')

    con.commit()
    con.close()

def Main():
    con = sqlite3.connect(r"C:\...\NomeFonte\...explorer.db")
    cur = con.cursor()

    # arquivo = r'D:\...\Fontes\..._.pas'
    # Interface, Implementation = GetUses(arquivo)
    # print('Interface:', '\n', Interface, '\n'*2)
    # print('Implementation:', '\n', Implementation)
    execute = cur.execute('SELECT codigo, caminho||"\\"||arquivo from arquivos WHERE extensao = ".pas"')
    ListaArquivo = execute.fetchall()
    con.close()

    for arquivo in ListaArquivo:
        codigo, arq = arquivo
        Interface, Implementation = GetUses(arq)

        SalvarFontes(con, codigo, Interface, Implementation)

        print(Interface) 
        print(Implementation, '\n')

Main()