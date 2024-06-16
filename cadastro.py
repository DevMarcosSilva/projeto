class Cadastro:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, primeiro_nome, ultimo_nome, idade, email, endereco, setor):
        usuario = {
            'id': len(self.usuarios) + 1,
            'primeiro_nome': primeiro_nome,
            'ultimo_nome': ultimo_nome,
            'idade': idade,
            'email': email,
            'endereco': endereco,
            'setor': setor
        }
        self.usuarios.append(usuario)

    def obter_usuarios(self):
        return self.usuarios

    def obter_usuario_por_id(self, user_id):
        for usuario in self.usuarios:
            if usuario['id'] == user_id:
                return usuario
        return None

    def editar_usuario(self, user_id, primeiro_nome, ultimo_nome, idade, email, endereco, setor):
        for usuario in self.usuarios:
            if usuario['id'] == user_id:
                usuario['primeiro_nome'] = primeiro_nome
                usuario['ultimo_nome'] = ultimo_nome
                usuario['idade'] = idade
                usuario['email'] = email
                usuario['endereco'] = endereco
                usuario['setor'] = setor
                break

    def excluir_usuario(self, user_id):
        self.usuarios = [usuario for usuario in self.usuarios if usuario['id'] != user_id]
