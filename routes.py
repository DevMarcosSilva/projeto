from flask import render_template, request, redirect, url_for
from cadastro import Cadastro

cadastro = Cadastro()

def setup_routes(app):
    @app.route('/')
    def index():
        # Renderiza o template 'index.html' quando a rota raiz é acessada
        return render_template('index.html')

    @app.route('/cadastro', methods=['GET', 'POST'], endpoint='cadastro')
    def cadastro_route():
        if request.method == 'POST':
            # Captura os dados do formulário
            primeiro_nome = request.form['first_name']
            ultimo_nome = request.form['last_name']
            idade = request.form['age']
            email = request.form['email']
            endereco = request.form['address']
            setor = request.form['setor']

            # Verifica se todos os campos foram preenchidos
            if primeiro_nome and ultimo_nome and idade and email and endereco and setor:
                # Adiciona o novo usuário ao cadastro
                cadastro.adicionar_usuario(primeiro_nome, ultimo_nome, idade, email, endereco, setor)
                # Redireciona para a lista de usuários após o cadastro
                return redirect(url_for('listar_usuarios'))
            else:
                # Exibe uma mensagem de erro se algum campo não foi preenchido
                msg = '*Preencha todos os campos'
                return render_template('cadastro.html', msg=msg)
        # Renderiza o template de cadastro se o método for GET
        return render_template('cadastro.html')

    @app.route('/usuarios', endpoint='listar_usuarios')
    def listar_usuarios():
        # Obtém a lista de usuários cadastrados
        usuarios = cadastro.obter_usuarios()
        # Renderiza o template 'usuarios.html' com a lista de usuários
        return render_template('usuarios.html', usuarios=usuarios)

    @app.route('/editar/<int:user_id>', methods=['GET', 'POST'], endpoint='editar_usuario')
    def editar_usuario(user_id):
        # Obtém o usuário pelo ID
        usuario = cadastro.obter_usuario_por_id(user_id)
        if request.method == 'POST':
            # Captura os dados do formulário de edição
            primeiro_nome = request.form['primeiro-nome']
            ultimo_nome = request.form['ultimo-nome']
            idade = request.form['idade']
            email = request.form['email']
            endereco = request.form['endereco']
            setor = request.form['setor']

            # Verifica se todos os campos foram preenchidos
            if primeiro_nome and ultimo_nome and idade and email and endereco and setor:
                # Atualiza os dados do usuário
                cadastro.editar_usuario(user_id, primeiro_nome, ultimo_nome, idade, email, endereco, setor)
                # Redireciona para a lista de usuários após a edição
                return redirect(url_for('listar_usuarios'))
        # Renderiza o template de edição com os dados do usuário
        return render_template('editar.html', usuario=usuario)

    @app.route('/excluir/<int:user_id>', methods=['POST'], endpoint='excluir_usuario')
    def excluir_usuario(user_id):
        # Exclui o usuário pelo ID
        cadastro.excluir_usuario(user_id)
        # Redireciona para a lista de usuários após a exclusão
        return redirect(url_for('listar_usuarios'))
