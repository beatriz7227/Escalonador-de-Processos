from src.leitor import carregar_sistema
from src.filas import Filas

def main():
    print("Carregando sistema...")
    quantum, tabela_processos = carregar_sistema("programas")
    print(f"\nQuantum definido: {quantum}")

    print("Tabela de Processos Carregada:")
    for processo in tabela_processos:
        print(processo)

    filas = Filas()
    filas.inicializar_processos(tabela_processos)

    print("Tabela de Processos Ordenada:")
    for processo in filas.fila_prontos:
        print(processo)

if __name__ == "__main__":
    main()