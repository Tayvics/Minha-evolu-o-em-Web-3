<div align="center">

# 🌐 Desenvolvimento Web III

<p align="center">
  <b>Repositório de estudos e práticas em Python e Flask</b><br>
  <i>Curso Superior de Tecnologia em Sistemas para Internet — IFRO Campus Porto Velho Zona Norte</i>
</p>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Evolução-ff69b4?style=for-the-badge)

</div>

<br>

## 📖 Sobre o Repositório

Este repositório reúne os exercícios, anotações e códigos desenvolvidos durante as aulas da disciplina de **Desenvolvimento Web III**, ministrada pela professora **Mariela Mizota Tamada**.

O foco é o desenvolvimento web com **Back-End em Flask**, renderização com **Jinja2**, rotas dinâmicas, formulários e arquivos estáticos. APIs, integração com banco de dados e deploy também fazem parte da trilha de estudos.

**Acadêmica:** Tayná Vitória Queiroz Moraes.

O repositório também é utilizado na atividade individual de **Controle de versões com GitHub**, com registro da evolução por commits e organização em branches.

---

## 📂 Estrutura do Projeto

A estrutura inicial dos exercícios foi organizada da seguinte forma:

```text
projeto_dw3/
├── templates/
│   ├── contato.html
│   ├── homepage.html
│   ├── index.html
│   ├── rota2.html
│   └── usuario.html
├── .gitignore
├── appFlask.py
├── importando.py
└── requirements.txt
```

Na versão utilizada para finalizar a atividade, o arquivo principal é **appFlask_v8.py**, e os templates com herança são carregados da pasta **t_templates/**.

Os principais arquivos utilizados nessa versão são:

```text
Minha-evolu-o-em-Web-3/
├── t_templates/
│   ├── base.html                       # Estrutura compartilhada e menu
│   ├── t_index.html                    # Página inicial
│   ├── t_contato.html                  # Página de contato
│   ├── t_usuario.html                  # Perfil com dados dinâmicos
│   ├── t_login.html                    # Exercício inicial de formulário
│   └── t_login_flash_js_cadastro.html  # Formulário com mensagens flash
├── static/
│   ├── css/
│   │   └── estilo.css
│   └── img/
│       └── logo.png
├── .gitignore
├── appFlask_v8.py                     # Aplicação principal da entrega
└── requirements.txt
```

A configuração `template_folder="t_templates"` informa ao Flask onde estão os templates dessa aplicação.

Para atender à proposta de versionamento, as versões anteriores da aplicação devem ser consultadas pelo histórico de commits, mantendo um único arquivo Python principal na versão final.

---

## 🚀 Como Executar Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Tayvics/Minha-evolu-o-em-Web-3.git
cd Minha-evolu-o-em-Web-3
```

### 2. Selecionar a branch da atividade

Após a publicação da branch de herança de templates:

```bash
git switch heranca-templates
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Instalar as dependências

No Windows, pelo PowerShell, é possível usar diretamente o Python do ambiente virtual, sem ativá-lo:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

### 5. Executar a aplicação

```powershell
& ".\.venv\Scripts\python.exe" appFlask_v8.py
```

Acesse:

http://127.0.0.1:8000

O terminal deve permanecer aberto durante os testes. Para encerrar o servidor, pressione **Ctrl+C**.

### Alternativa: ativação do ambiente virtual

No Windows, pelo PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Windows, pelo Prompt de Comando:

```bat
.venv\Scripts\activate.bat
```

Após a ativação:

```bash
python -m pip install -r requirements.txt
python appFlask_v8.py
```

O ambiente virtual é utilizado apenas localmente e não deve ser enviado ao GitHub.

---

## 📌 Trilha de Aprendizado & Conteúdos

- [x] Aula 00: Apresentação da disciplina, ementa e arquitetura MVC.
- [x] Aula 01: Evolução da Web — Web 1.0 à 4.0 e Edge Computing.
- [x] Aula 02: Ambientes virtuais, configuração do VS Code e introdução ao Flask.
- [x] Aula 03 — Parte 1: Renderização de templates Jinja2 e rotas com passagem de parâmetros.
- [x] Aula 03 — Parte 2: Herança de templates, arquivos estáticos, CSS e imagens.
- [x] Aula 03 — Parte 3: Implementação de requisições GET/POST e mensagens flash.
- [ ] Próximos passos: Persistência em banco de dados, APIs RESTful e deploy.

---

## 🕓 Histórico de Evolução

Os commits registram as alterações realizadas ao longo das aulas.

| Commit | Descrição da evolução |
|---|---|
| `60e6a19` | Estrutura inicial com Flask, templates HTML, dependências e configuração do `.gitignore`. |
| `17e2677` | Complementação dos exercícios, alterações nos templates e inclusão do README. |
| `0072298` | Introdução da herança de templates com `base.html`, páginas derivadas e imagem estática. |
| `114695c` | Inclusão de CSS, atualização da base e formulário de login. |
| `45f0ea9` | Inclusão da rota de autenticação e exercícios com GET e POST. |
| `788beae` | Inclusão de exercícios de JavaScript e versões com autenticação e cadastro. |

Os ajustes finais da atividade incluem a personalização da instância Flask, a correção dos nomes utilizados no menu e a padronização da herança dos templates.

Para consultar o histórico:

```bash
git log --oneline --all --graph
```

Para visualizar as alterações de um commit:

```bash
git show IDENTIFICADOR_DO_COMMIT
```

---

## 🌿 Organização das Branches

A organização prevista para a entrega utiliza:

| Branch | Finalidade |
|---|---|
| `main` | Histórico principal dos exercícios desenvolvidos durante as aulas. |
| `heranca-templates` | Ajustes da versão com herança de templates e preparação da entrega. |

A branch `heranca-templates` deve conter um commit próprio com as alterações realizadas, além de ser enviada ao GitHub.

Para listar as branches:

```bash
git branch -a
```

Para trocar de branch:

```bash
git switch main
git switch heranca-templates
```

---

## 🧪 Testes e Evidências

As evidências devem apresentar capturas do navegador, identificar as versões pelos commits e explicar as mudanças observadas.

| Funcionalidade | Verificação | Situação |
|---|---|---|
| Página inicial | Exibição do menu, logo e conteúdo da página. | Abertura confirmada. |
| Perfil do usuário | Exibição do conteúdo após a correção do bloco de herança. | Abertura confirmada. |
| Login | Renderização do formulário após a correção do template base. | Abertura confirmada. |
| Autenticação válida | Envio de credenciais válidas e conferência da resposta. | Validação pendente. |
| Autenticação inválida | Envio de credenciais inválidas e conferência das mensagens flash. | Validação pendente. |
| Comparação entre versões | Capturas que demonstrem a diferença visual entre dois commits. | Documentação pendente. |

Exemplo de acesso à rota dinâmica:

```text
http://127.0.0.1:8000/usuario/Tayna;Assistente%20de%20TI
```


### Referências para consulta

- Documentação do Git: https://git-scm.com/docs
- Livro Pro Git: https://git-scm.com/book/pt-br/v2
- Documentação do GitHub: https://docs.github.com/pt

---

## ✅ Checklist da Entrega

- [x] Conta e repositório no GitHub.
- [x] Histórico com seis commits anteriores aos ajustes finais.
- [x] README com descrição do projeto e evolução.
- [x] Pesquisa teórica registrada neste README.
- [ ] Conferir a existência de um único arquivo Python principal na versão final.
- [ ] Conferir a personalização da instância Flask e dos decoradores com o nome da acadêmica.
- [ ] Registrar e publicar o commit de ajustes na branch `heranca-templates`.
- [ ] Validar a autenticação com credenciais corretas e incorretas.
- [ ] Salvar no GitHub o documento de evidências com comparação entre versões.
- [ ] Confirmar o acesso solicitado para `mariela.tamada@ifro.edu.br`.
- [ ] Testar o acesso ao repositório com outra conta.
- [ ] Enviar o documento único no AVA dentro do prazo.

**Observação:** as marcações pendentes devem ser atualizadas após a conclusão e conferência de cada etapa.