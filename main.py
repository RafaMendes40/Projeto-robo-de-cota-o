from Extrator import buscar_dados_iphone
from Processador import salvar_em_excel

print("Iniciando a Busca:")
lista_de_celulares = buscar_dados_iphone("Iphone 15")

print(lista_de_celulares)

salvar_em_excel(lista_de_celulares)
