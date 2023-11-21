#!/usr/bin/env python3
import tkinter as tk
from tkinter import simpledialog
import os

def obter_diretorio_e_nome_arquivo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    diretorio = simpledialog.askstring("Diretório", "Digite o caminho do diretório:")
    nome_arquivo = simpledialog.askstring("Nome do Arquivo", "Digite o nome do arquivo:")

    return diretorio, nome_arquivo

def encontrar_arquivo(diretorio, nome_arquivo):
    for arquivo in os.listdir(diretorio):
        if nome_arquivo in arquivo:
            return os.path.join(diretorio, arquivo)
    return None

def realizar_substituicoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].replace("SigChaveDistrib", "SigSeccionadora")
        linhas[i] = linhas[i].replace("NE 0 9", "NE 0 2")

        if "{}" in linhas[i]:
            parametros = linhas[i].split('{')[1].split('}')[0].split()

            # Manter os parâmetros desejados
            novos_parametros = parametros[10:12] + parametros[14:16]

            # Substituir os 18 parâmetros originais pelos novos
            linhas[i] = linhas[i].replace("{" + " ".join(parametros) + "}", "{" + " ".join(novos_parametros) + "}")

        if "}" in linhas[i]:
            linhas[i] = "} 2 { BRANCO IGN } INDQ_IGN"

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

def main():
    diretorio, nome_arquivo = obter_diretorio_e_nome_arquivo()

    if diretorio and nome_arquivo:
        caminho_completo = encontrar_arquivo(diretorio, nome_arquivo)

        if caminho_completo:
            print(f"Caminho completo do arquivo: {caminho_completo}")

            realizar_substituicoes(caminho_completo)

            print("Substituições realizadas com sucesso!")
        else:
            print(f"Arquivo {nome_arquivo} não encontrado no diretório {diretorio}")

if __name__ == "__main__":
    main()
