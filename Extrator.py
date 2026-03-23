from playwright.sync_api import sync_playwright
import time

def buscar_dados_iphone(produto_busca):
    dados = []

    with sync_playwright() as pw:
        navegador = pw.chromium.launch(headless=False)
        
        contexto = navegador.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        pagina = contexto.new_page()
    
        print("Acessando o Mercado Livre...")
        pagina.goto("https://www.mercadolivre.com.br/")
        
        print("Aguardando carregamento (resolva o Captcha se aparecer)...")
        pagina.wait_for_timeout(5000) 

        barra_pesquisa = pagina.locator("input#cb1-edit")
        
        if barra_pesquisa.is_visible():
            barra_pesquisa.fill(produto_busca)
            barra_pesquisa.press("Enter")
 
            print("Enter pressionado! Aguardando a lista de produtos...")

            # Esperar a lista de produtos carregar na tela
            pagina.wait_for_selector(".ui-search-layout__item")
            produtos = pagina.locator(".ui-search-layout__item").all()

            print(f"Sucesso! Encontrei {len(produtos)} produtos na tela, lendo dados")

            for produto in produtos:
                try:
                    titulo = produto.locator("h2, h3, .ui-search-item__title, .poly-component__title").first.inner_text(timeout=2000)
                    preco_texto = produto.locator(".andes-money-amount__fraction, .poly-price__current").first.inner_text(timeout=2000)
                    preco_numerico = float(preco_texto.replace(".", ""))
                    
                    dados.append({
                        "Modelo": titulo,
                        "Preço (R$)": preco_numerico
                    })
                    print("Salvo: {titulo} - R$ {preco_numerico}")
                except Exception as e:
                    print(f"Erro ao ler um produto: {e}")
                    continue
       
        navegador.close()

    return dados






