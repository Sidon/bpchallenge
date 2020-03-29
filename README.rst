###############################
``Brasilprev - Desafio Python``
###############################

*****
TL;DR
*****

| Application front end: http://tiny.cc/sdnbptest-frontend
| API Postman Documentation: http://tiny.cc/sdnbptest-postman
| Continuous Integration Tests: http://tiny.cc/sdnbptest-travis
| Github repo: http://tiny.cc/sdnbptest-github
| Application hosted in  http://www.heroku.com.

***************
Execução local
***************

Obtendo o código
*****************

* Clone o repositorio: http://tiny.cc/sdnbptest-github
* Crie um ambiente virtual com seu gerenciador favorito (conda, pyenv, virtualenv, etc);

Utilizando o Docker
********************

.. code-block::

   $ cd <path/direotiro/clonado>
   $ docker build . -t bprev
   $ docker run -d -p 8030:8030 bprev

* Aponte o browse para http://localhost:8030/


Sem a utilização do docker
**************************

* Após clonar o repositorio;
* Crie um ambiente virtual com seu gerenciador favorito (conda, pyenv, virtualenv, etc);
* Ative o ambiente criado e instale os requirements
* Execute o servidor com o comando ``python manager.py runserver``
* Aponte o browser para ``localhost:8000``

*********************
Descrição do desafio
*********************

Você foi convidado a realizar um desafio para a vaga de desenvolvedor(a)
back-end Python. Queremos avaliar sua qualidade de código, capacidade de
análise, resolução de problemas e principalmente sua criatividade.

Construa uma API REST para simular uma loja virtual. Esta loja deve ter um
cadastro de seus clientes, produtos e pedidos. Fique à vontade para escolher como
fará a arquitetura do sistema, bem como frameworks que utilizará.



******************************
Descrição da solução proposta
******************************
A applicação está sendo desenvolvida em python/django, tanto no backend (API REST) como no front-end,
contendo 4 subapps (Authenticacao, Customer, Iem e Order). A utilização da api só poderá ser feita após a obtenção do
token, com exceção do cadastro do cliente.

Banco de dados
**************
Para simplificar foi utilizado o banco de dados "embutido" no python SQLite3.

Front end
*********

Todas as funcionalidades serão disponibilizadas no backend via API REST. Um frontend foi desenvolvido apenas para
essa documentação.

*****************************
Ambiente de desenvolvimento:
*****************************

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


*******************
Cobertura (Pytest)
*******************
Em função do tempo a opção foi fazer o minimo de teste possível somente para demonstrar a técnica.
O pacote utilizado para o testes foi o pytest: https://docs.pytest.org/en/latest/

:Date: **27/03/2020**
:Author:  **Sidon Duarte**

