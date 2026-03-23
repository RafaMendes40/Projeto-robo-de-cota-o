import pandas as pd

def salvar_em_excel(dados, nome_arquivo="cotacao_iphones.xlsx"):
    if not dados:
        print("A lista está vazia, nenhum arquivo foi gerado")
        return
    
    print("Iniciando a criação da planinha")

    tabela = pd.DataFrame(dados)
    tabela.to_excel(nome_arquivo, index=False)

    print(f"Sucesso! Planinha '{nome_arquivo}' gerada na sua pasta")

    
