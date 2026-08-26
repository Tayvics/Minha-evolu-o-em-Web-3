from flask import Flask, render_template

meu_site = Flask(__name__)

@meu_site.route('/')
@meu_site.route('/ola')
def raiz():
    return render_template('homepage.html')

@meu_site.route('/index')
def index():
    return render_template('index.html')

@meu_site.route('/contato')
def contato():
    return render_template('contato.html')

@meu_site.route('/usuario')
def dados_usuario():
    dados_usu = {"nome": "Mariela", "profissao": "Professora EBTT", "disciplina": "Desenvolvimento Web III"}
    return render_template("usuario.html", dados=dados_usu)

@meu_site.route('/rota2')
def rota2():
    return render_template('rota2.html')

def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

## PAGINA DINÂMICA. PRECISA DE 3 ELEMENTOS: DADOS DINÂMICOS NA URL ENTRE <>, 
## OS PARAMETROS NA FUNÇÃO E PÁGINA MONTADA
"""
EXERCÍCIO #3: PÁGINAS DINÂMICAS VIA URL
Conceito: Substitui valores estáticos no código por dados dinâmicos passados diretamente pela URL.

Requer 3 elementos fundamentais:
1. Variáveis dinâmicas na rota delimitadas por < >.
2. Parâmetros correspondentes na assinatura da função def().
3. Envio dos dados para o Jinja2 via render_template(..., variavel=valor).
"""
@meu_site.route('/ola/<id>')
def saudar(id):
    return render_template('homepage.html', nome=id)

@meu_site.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usuario={"nome": p_nome, "profissao": p_profissao, "disciplina": p_disciplina}
    return render_template("usuario.html", dados = dados_usuario)

if __name__ == '__main__':
    meu_site.run(port=7000, debug=True)



