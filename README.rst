###############################
``Brasilprev - Desafio Python``
###############################


Descrição
**********

Você foi convidado a realizar um desafio para a vaga de desenvolvedor(a)
back-end Python. Queremos avaliar sua qualidade de código, capacidade de
análise, resolução de problemas e principalmente sua criatividade.

Construa uma API REST para simular uma loja virtual. Esta loja deve ter um
cadastro de seus clientes, produtos e pedidos. Fique à vontade para escolher como
fará a arquitetura do sistema, bem como frameworks que utilizará.


TL;DR
*******
| A aplicação está hospedada no Heroku http://www.heroku.com.
| Para testá-la clique: coming soon
| Repositorio no github: coming soon
| Documentação REST API: coming soon
| Testes (Integração): coming soon


DESCRIÇÃO DA SOLUÇÃO PROPOSTA
*****************************
A applicação está sendo desenvolvida em python/django, tanto no backend (API REST) como no front-end,
contendo 4 subapps (Authenticacao, Customer, Iem e Order). A utilização da api só poderá ser feita após a obtenção do
token.

Dados iniciais:
Para simplificar foi utilizado o banco de dados "embutido" no python SQLite3,

Todas as funcionalidades serão disponibilizadas no backend via API REST. Um frontend será desenvolvido apenas para
essa documentação

Ambiente de desenvolvimento:
****************************

    +-------------------+---------------------------+------------+
    | Resource          | Description               | Version    |
    +===================+===========================+============+
    | Computer          | Desktop 16 GB Memory      | I5 G5      |
    +-------------------+---------------------------+------------+
    | Operating System  | Ubuntu  LTS               | 18.04      |
    +-------------------+---------------------------+------------+
    | Editor/IDE        | Pycharm                   | 2019.3     |
    +-------------------+---------------------------+------------+
    | venv              | Conda (Miniconda)         | 4.7.12     |
    +-------------------+---------------------------+------------+
    | Devel Platform    + Django/Python             | 3.8        |
    +-------------------+---------------------------+------------+
    | CI                | travis-ci                 | 2020       |
    +-------------------+---------------------------+------------+
    | Coverage          | Pytest --cov              | 2.8.1      |
    +-------------------+---------------------------+------------+
    | Django            | Main framework            | 3.0.3      |
    +-------------------+---------------------------+------------+
    | DRF               | dajano-rest-fw            |  4.4.0     |
    +-------------------+---------------------------+------------+

:Date: **03/03/2020**
:Author: **Sidon Duarte**

Cobertura (Pytest)
******************

.. code-block::



###########################
Documentação da  API (REST)
###########################

Para a documentação foi utilizado a versão free do software para desenvolvimento de APIs `Postman <https://www.postman.com/>`_.
A documentação oferece exemplos de requests em varios formatos, tais como cURL, c#, Go, HTTP, Javascrip, Java, Etc.
Para acessar clique no link: https://documenter.getpostman.com/view/3684623/SzKYNGXQ

Testes
******
Para testar a api, além do Postman citado, foi utilizado também o pacote `Pytest <https://docs.pytest.org/en/latest/>`_.

Instalação local
****************

Clone o repositorio coming soon;

Crie um ambiente virtual com seu gerenciador favorito (conda, pyenv, virtualenv, etc);

Crie uma variável de ambiente chamada ENVIRONMENT com o valor 'local':

.. code-block::

    $ export ENVIRONMENT='local'

No diretorio clonado, instale os requirements com o comando:

.. code-block::

    $ pip install -r dev_requirements.txt

Crie os dados iniciais com o comando:

.. code-block::

    $ python ./manage.py initial_data

Execute a aplicação com o comando:

.. code-block::

    $ python ./manage.py runserver
