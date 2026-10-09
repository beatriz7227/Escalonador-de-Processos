from src.leitor import carregar_sistema

def main():
    print("Carregando sistema...")
    quantum, tabela_processos = carregar_sistema("programas")
    print(f"\nQuantum definido: {quantum}")
    print("Tabela de Processos Carregada:")
    for processo in tabela_processos:
        print(processo)

if __name__ == "__main__":
    main()