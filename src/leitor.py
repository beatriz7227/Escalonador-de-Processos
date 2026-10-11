import os
from src.bcp import BCP

def carregar_sistema(caminho_pasta="programas"):
    # lê a configuração de quantum determinada para a execução
    caminho_quantum = os.path.join(caminho_pasta, "quantum.txt")
    with open(caminho_quantum, "r") as f:
        quantum = int(f.readline().strip())

    # lê a lista de prioridades
    caminho_prioridade = os.path.join(caminho_pasta, "prioridades.txt")
    with open(caminho_prioridade, "r") as f:
        prioridades = [int(linha.strip()) for linha in f if linha.strip()]

    ficheiros = sorted(os.listdir(caminho_pasta))
    ficheiros_programas = [f for f in ficheiros if f.endswith(".txt") and f not in ["quantum.txt", "prioridades.txt"]]
    
    tabela_processos = []

    # faz o parse de cada programa para inicializar o seu BCP
    for i, nome_ficheiro in enumerate(ficheiros_programas):
        caminho_completo = os.path.join(caminho_pasta, nome_ficheiro)
        with open(caminho_completo, "r") as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
            
        nome_programa = linhas[0]     
        instrucoes = linhas[1:]       
        prioridade = prioridades[i]    
        
        bcp = BCP(nome_programa, instrucoes, prioridade)
        tabela_processos.append(bcp)

    return quantum, tabela_processos