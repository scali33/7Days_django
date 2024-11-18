Desafio Alura: Consumindo uma API com Django

Este projeto foi desenvolvido como parte de um desafio da Alura, onde o objetivo era criar uma aplicação utilizando o framework Django para consumir e exibir dados de uma API relacionada ao universo do desenho Avatar: A Lenda de Aang.
Funcionalidades

Consumo e exibição de informações detalhadas sobre personagens do desenho Avatar.
Paginação dinâmica para navegar entre diferentes personagens.
interface amigável e estilizada com Bootstrap para uma melhor experiência do usuário.

Tecnologias utilizadas

Python 3 com Django como framework principal.
Bootstrap 5 para estilização da interface.
Consumo de dados via API RESTful.

Como executar o projeto

    Clone o repositório para sua máquina:

    git clone <URL_DO_REPOSITORIO>

Acesse a pasta do projeto:

    cd nome_do_projeto

Crie um ambiente virtual e ative-o:

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

Instale as dependências:

    pip install -r requirements.txt

Execute o servidor de desenvolvimento:

    python manage.py runserver

Acesse o projeto no navegador através de:

    http://127.0.0.1:8000/

Aprendizados

Durante o desenvolvimento, foram explorados conceitos como:

Consumo de APIs externas com o requests.
Organização de templates e views no Django.
Paginação e navegação entre dados consumidos dinamicamente.
Estilização responsiva com Bootstrap.
