# Programação Backend
Atividades das aulas de Programação Backend no SENAI, utilizando Django e Django REST Framework.

<div style="display: flex;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" style="width:100px;" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" style="width:100px;" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-original.svg" style="width:100px;" />
</div>

O objetivo do projeto é criar uma API para o sistema de uma livraria completamente funcional.
Acessar em http://127.0.0.1:8000/

## Aula 01 (01/08/2025): Configuração inicial do ambiente virtual
- Criação do ambiente virtual (python -m venv env)
- Instalação do Django, Django REST Framework e Django Cors Headers (pip install djangorestframework django-cors-headers)
- Criação do requirements.txt (pip freeze > requirements.txt)
- Criação do projeto e da aplicação Django (django-admin startproject livraria . ; django-admin startapp api)
- Upload do projeto no Github

## Aula 02 (07/08/2025): Início do desenvolvimento do projeto
- Instalação do Pandas (pip install pandas)
- Primeira inicialização do projeto (py manage.py runserver)
- Criação do modelo Author em models.py
- Criação das migrações (py manage.py makemigrations)
- Migração (py manage.py migrate)
- Acesso ao /admin
- Criação do usuário administrador admin (senha: 123) (py manage.py createsuperuser)
- Criação da URL para a API (http://127.0.0.1:8000/api/)
- Criação dos serializers do Rest Framework
- Criação das views
- Criação da URLs intrínsecas à API
- Registro da API em admin

## Aula 03 (08/08/2025): Cinema
- Absolute cinema
- ### Framework
  - Aglomerado de bibliotecas
  - Facilitador para o desenvolvimento em volta de certa linguagem
- ### MVC Pattern
  - Model - View - Controller
  - Usuário -> Controller -> Model -> Controller -> View -> Controller -> Usuário
  - Model: Lógica dos dados; interage com o banco de dados
  - View: Apresentação dos dados
  - Controller: Controla requisições e comunicação View-Model
- ### API
  - Centro entre comunicação front-back pela internet
  - Comunicação HTTP
  - Endpoint
    - Caminho Back-Front