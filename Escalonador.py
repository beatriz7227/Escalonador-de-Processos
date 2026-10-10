from src.leitor import carregar_sistema
from src.filas import Filas
from src.interpretador import Interpretador

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

    interpretador = Interpretador(quantum, tabela_processos)
    interpretador.executar()
    for linha in interpretador.linhas_log:
        print(linha)

        
    est = interpretador.estatisticas()
    print(f"MEDIA DE TROCAS: {est['media_trocas']}")
    print(f"MEDIA DE INSTRUCOES: {est['media_instrucoes']}")
    print(f"QUANTUM: {est['quantum']}")

if __name__ == "__main__":
    main()