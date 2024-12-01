import os

def listar_arquivos_recursivamente(diretorio, nivel=0):
    try:
        itens = os.listdir(diretorio)
        
        for item in itens:
            caminho_completo = os.path.join(diretorio, item)
            
            if os.path.isdir(caminho_completo):
                print("  " * nivel + f"[SUBDIRETÓRIO] {item}")
                listar_arquivos_recursivamente(caminho_completo, nivel + 1)
            else:
                print("  " * nivel + f"[ARQUIVO] {item}")
    except PermissionError:
        print("  " * nivel + "[ACESSO NEGADO]")

diretorio_inicial = os.path.join(os.getcwd(), "Questao_1\Documentos")

print(f"Listando arquivos e diretórios em: {diretorio_inicial}")
listar_arquivos_recursivamente(diretorio_inicial)
