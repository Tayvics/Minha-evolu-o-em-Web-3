<div align="center">

# 🌐 Desenvolvimento Web III

<p align="center">
  <b>Repositório de estudos e práticas em Python e Flask</b> <br>
  <i>Curso Superior de Tecnologia em Sistemas para Internet — IFRO Campus Porto Velho Zona Norte</i>
</p>

<!-- Badges Fofos e Tecnologias -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Evolução%20✨-ff69b4?style=for-the-badge)

</div>

<br>

## 📖 Sobre o Repositório

Este repositório reúne os exercícios, anotações e códigos desenvolvidos durante as aulas da disciplina de **Desenvolvimento Web III**, ministrada pela professora **Mariela Mizota Tamada**. 

O foco é o desenvolvimento web moderno com foco em **Back-End com Flask**, renderização com **Jinja2**, rotas dinâmicas, formulários, APIs e integração com banco de dados.

---

## 📂 Estrutura do Projeto

```text
projeto_dw3/
├── templates/               # 📑 Páginas HTML renderizadas pelo Jinja2
│   ├── contato.html         # Página de dados de contato
│   ├── homepage.html        # Página inicial de boas-vindas
│   ├── index.html           # Menu de navegação principal
│   ├── rota2.html           # Página de teste de rotas
│   └── usuario.html         # Exibição dinâmica de dados do usuário
├── .gitignore               # 🔒 Ignora ambientes locais (venv)
├── appFlask.py              # 🚀 Servidor Flask principal e rotas
├── importando.py            # 📦 Testes de modularização e importação
└── requirements.txt         # 📋 Lista de dependências do Python
```
## 🚀 Como Executar Localmente
1. Clonar o repositório e acessar a pasta
Bash
git clone [https://github.com/Tayvics/dw3.git](https://github.com/Tayvics/dw3.git)
cd dw3

2. Criar e ativar o ambiente virtual (venv)
No Windows (PowerShell):

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
No Windows (Prompt de Comando):

DOS
python -m venv venv
venv\Scripts\activate
3. Instalar as dependências
Bash
pip install -r requirements.txt
4. Executar o servidor
Bash
python appFlask.py
Acesse a aplicação em: http://127.0.0.1:7000

## 📌 Trilha de Aprendizado & Conteúdos
[x] Aula 00: Apresentação da disciplina, ementa e arquitetura MVC

[x] Aula 01: Evolução da Web (Web 1.0 à 4.0 e Edge Computing)

[x] Aula 02: Ambientes Virtuais (virtualenv), configuração do VS Code e introdução ao Flask

[x] Aula 03 (Parte 1): Renderização de templates Jinja2 e rotas com passagem de parâmetros

[ ] Aula 03 (Parte 2): Herança de templates (base.html), arquivos estáticos (CSS/imagens)

[ ] Aula 03 (Parte 3): Requisições GET vs. POST e mensagens flash()

[ ] Próximos passos: Persistência em Banco de Dados, APIs RESTful e Deploy