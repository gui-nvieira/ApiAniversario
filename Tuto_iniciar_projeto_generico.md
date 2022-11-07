#Como fazer a venv pelo powershell do windows?

Acesse a pasta do seu projeto usando:
`cd nome_da_pasta`
e digite o seguinte comando:
`python3 -m venv venv`

##Para ativar o seu ambiente virtual
Acesse a pasta principal do seu projeto e digite o comando:
`venv\Scripts\activate`

##Para desativar
Basta que execute o comando:
`deactivate`

##Como fazer uma variável local usando Windows (+Powershell)?
`$env:SUA_VARIAVEL = 'valor_da_variavel.py'`

para definir a variavel de ambiente(flask) utilize:
`$env:FLASK_APP = 'main.py'`

para visualizar a variavel use:
`$env:SUA_VARIAVEL`

depois vá na pasta onde está a main usando:
`cd nome_da_pasta`

e rode o flask usando:
`python -m flask run`
