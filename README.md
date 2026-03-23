WEB SCRAPER e ETL - Cotação de preços no site mercado livre

 Este projeto se consiste em uma automaçaõ desenvolvida em python, para realizar a extração de dados, de produtos no mercado livre, aplicando conceitos fundamenteis de ETL

 O script tem como objetivo: nevegar no site de forma automizada, contornando bloqueios basicos de detecção de bots, extrai os nomes e preços de produtos pesquisados e armazena numa planinha do excel para analise:

 ## Bibiotecas utilizadas:
 -Python 3
 -Playwright
 -Pandas
 -Openpyxl

## Arquitetura do Projeto
O Codigo foi costruido em 3 arquivos principais, utilizando o principio de separação de resposabilidade.
(Também possibilitando de utilizar outros produtos para fazer a extração de dados)

1. Extrator.py: Configura o playwright como um "user-agent", acessando o site do mercado livre, e buscando as cotações de preço de Iphones
2. Processador.py: Recebe os dados extraidos, e utilizando o pandas, converte em um Dataframe e exporta o resultado em uma planinha do Excel.
3. Main.py: O ponto de entrada da aplicação. Faz a comunicação entre o Extrator e o Processador.

## Como executar este projeto na sua maquina

### Pré-Requisitos
Python instalado no seu computador
Visual code (Ou outra IDE que utilizar)

2. (IMPORTANTE) Crie e ative um ambiente virtual
  - WINDOWS: no terminal do seu visual code, utilize o comando: python -m venv venv e para a ativar: .\venv\Scripts\Activate
  - Linux/MAC: python3 -m venv venv e source venv/bin/activate

3. Instalar a dependecias:
   pip install -r requirements.txt
   playwright install chromium

4. Execute o robo no Terminal utilizando o: python main.py
5. Ao Rodar o script o navegador será aberto brevemente e o terminal exibira a coleta em tempo real.
