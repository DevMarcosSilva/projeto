from flask import render_template, request, redirect, url_for
from cadastro import Cadastro

cadastro = Cadastro()

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cadastro', methods=['GET', 'POST'], endpoint='cadastro')
    def cadastro_route():
        if request.method == 'POST':
            primeiro_nome = request.form['first_name']
            ultimo_nome = request.form['last_name']
            idade = request.form['age']
            email = request.form['email']
            endereco = request.form['address']
            setor = request.form['setor']

            if primeiro_nome and ultimo_nome and idade and email and endereco and setor:
                cadastro.adicionar_usuario(primeiro_nome, ultimo_nome, idade, email, endereco, setor)
                return redirect(url_for('listar_usuarios'))
            else:
                msg = '*Preencha todos os campos'
                return render_template('cadastro.html', msg=msg)
        return render_template('cadastro.html')

    @app.route('/usuarios', endpoint='listar_usuarios')
    def listar_usuarios():
        usuarios = cadastro.obter_usuarios()
        return render_template('usuarios.html', usuarios=usuarios)

    @app.route('/editar/<int:user_id>', methods=['GET', 'POST'], endpoint='editar_usuario')
    def editar_usuario(user_id):
        usuario = cadastro.obter_usuario_por_id(user_id)
        if request.method == 'POST':
            primeiro_nome = request.form['first_name']
            ultimo_nome = request.form['last_name']
            idade = request.form['age']
            email = request.form['email']
            endereco = request.form['address']
            setor = request.form['setor']

            if primeiro_nome and ultimo_nome and idade and email and endereco and setor:
                cadastro.editar_usuario(user_id, primeiro_nome, ultimo_nome, idade, email, endereco, setor)
                return redirect(url_for('listar_usuarios'))
            else:
                msg = '*Preencha todos os campos'
                return render_template('editar.html', usuario=usuario, msg=msg)
        return render_template('editar.html', usuario=usuario)

    @app.route('/excluir/<int:user_id>', methods=['POST'], endpoint='excluir_usuario')
    def excluir_usuario(user_id):
        cadastro.excluir_usuario(user_id)
        return redirect(url_for('listar_usuarios'))
