# Web_Scrapping

Sempre fui muito apaixonado pela área de dados. Neste projeto destaco um dos ponto importantissímos, para uma análise de dados mais profunda e compreensível: A extração dos dados. Existem diversas maneiras de extrair os dados, neste projeto meu foco foi entender mais profundamente como funciona a extração dos dados usando Web_scrapping. Os dados que foram coletados são brutos, ou seja, não passou por um tratamento.

## O que é Web Scrapping?

É o processo de coletar informações ou dados de websites da internet de forma automatizada. Essa técnica envolve o uso de programas de computador (ou bots) para navegar por páginas da web, extrair dados de interesse e, em seguida, armazená-los para análise, visualização, pesquisa ou qualquer outro propósito.


## Alguns exemplos de como é usado:

Coleta de Dados: Extrair informações, como preços de produtos, avaliações de usuários, notícias, informações de contato, entre outros, de sites da web.

Monitoramento: Acompanhar mudanças em sites, como preços de produtos ou atualizações de conteúdo, e notificar quando ocorrem alterações.

Análise de Dados: Utilizar os dados coletados para análise estatística, pesquisa de mercado, previsões, e tomada de decisões informadas.

Comparação de Preços: Comparar preços de produtos em diferentes sites de comércio eletrônico.

Integração de Dados: Integrar dados de várias fontes da web em um único banco de dados ou sistema.

Indexação de Conteúdo: Coletar dados para mecanismos de pesquisa e indexação de conteúdo, como o Google.


## Ferramentas utilizadas:

Antes de executar o script, certifique-se de ter as seguintes bibliotecas Python instaladas:

- BeautifulSoup (bs4)
- requests
- re
- pandas
- math

Você pode instalar essas bibliotecas usando o pip, caso ainda não estejam instaladas.

## Defina a URL de destino:

url_pag = f'https://www.kabum.com.br/computadores/notebooks?page_number={i}2&page_size=20&facet_filters=&sort=most_searched'


Importante: A url está modificada para o laço de repetição conforme a busca pelos preços dos notebooks. Caso queira buscar por outros produtos, altere o laço de repetição conforme o número de páginas que irá consultar. 


Você pode alterar a URL para direcionar a raspagem para diferentes categorias de produtos no site do Kabum.

Especifique o agente de usuário (user-agent):

Para fazer solicitações à web, é preciso definir uma string de agente de usuário no dicionário headers. Neste script, utilizou-se uma string de agente de usuário que simula um navegador Chrome.

Loop de Raspagem na Web:

O script envia uma solicitação para a URL especificada e analisa o conteúdo HTML usando o BeautifulSoup.
Ele obtém o número total de itens disponíveis para venda no site.
Calcula o número de páginas necessárias para raspar todos os itens.
Inicializa um dicionário vazio para armazenar informações dos produtos.
Iteração pelas Páginas:

O script percorre cada página de listagem de produtos. Para cada página:

Constrói a URL da página.
Envia uma solicitação e analisa o conteúdo HTML.
Extrai informações do produto, como marca e preço.
Anexa essas informações ao dicionário dic_products.
Criação de um DataFrame:

Após coletar todos os dados do produto, o script cria um DataFrame Pandas usando o dicionário dic_products.

Salva os Dados em um Arquivo CSV:

O script salva os dados em um arquivo CSV com o nome 'notebook_gamer.csv' usando a função to_csv do Pandas.

Você pode alterar o caminho e o nome do arquivo de acordo com suas preferências.


# Executando o Script


'''
python scrapping.py
'''




Observação: Dependendo do site, poderá estar sujeito a políticas de privacidade. É sempre importante conferir as informações para realizar a raspagem dos dados. Fique à vontade para forkar e clonar o projeto em sua máquina! 






