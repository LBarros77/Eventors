# AppEvents

Sistema Integrado de Gestão Eventos baseado em Django

Projeto desenvolvido em Python 3 no Windows, testado no GNU/Linux e Windows.


## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.7.5
- [django](http://www.djangoproject.com) == 3.1.14
- [geraldo](https://github.com/thiagopena/geraldo) - Geração de PDF para pedidos de venda/compra

## Instalação:

0. Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

2. Edite o conteúdo do arquivo **djangosige/configs/configs.py**

3. Gere um `.env` local

4. Sincronize a base de dados:

```bash
python manage.py migrate
```

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

```bash
python manage.py runserver
```

## Implementações

- Cadastro de produtos, clientes e empresas
- Login/Logout
- Criação de perfil para cada usuário.
- Definição de permissões para usuários.
- Criação e geração de PDF
- Interface simples e em português

## Tarefas para serem feitas
...

## Créditos

- [Leonardo Barros](https://github.com/gurayyarar/AdminBSBMaterialDesign)
- [Themesberg][https://demo.themesberg.com/]

## Ajuda

Para relatar bugs ou fazer perguntas utilize o email leonprogramer@gmail.com

Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.
