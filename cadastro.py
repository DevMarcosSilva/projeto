class Cadastro:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os usuários cadastrados
        self.usuarios = []

    def adicionar_usuario(self, primeiro_nome, ultimo_nome, idade, email, endereco, setor):
        # Cria um dicionário com as informações do usuário e um ID único
        usuario = {
            'id': len(self.usuarios) + 1,  # O ID é o tamanho atual da lista + 1, garantindo IDs únicos
            'primeiro_nome': primeiro_nome,
            'ultimo_nome': ultimo_nome,
            'idade': idade,
            'email': email,
            'endereco': endereco,
            'setor': setor
        }
        # Adiciona o novo usuário à lista de usuários
        self.usuarios.append(usuario)

    def obter_usuarios(self):
        # Retorna a lista de todos os usuários cadastrados
        return self.usuarios

    def obter_usuario_por_id(self, user_id):
        # Percorre a lista de usuários para encontrar aquele com o ID especificado
        for usuario in self.usuarios:
            if usuario['id'] == user_id:
                return usuario  # Retorna o usuário se encontrado
        return None  # Retorna None se o usuário com o ID especificado não for encontrado

    def editar_usuario(self, user_id, primeiro_nome, ultimo_nome, idade, email, endereco, setor):
        # Percorre a lista de usuários para encontrar aquele com o ID especificado
        for usuario in self.usuarios:
            if usuario['id'] == user_id:
                # Atualiza as informações do usuário
                usuario['primeiro_nome'] = primeiro_nome
                usuario['ultimo_nome'] = ultimo_nome
                usuario['idade'] = idade
                usuario['email'] = email
                usuario['endereco'] = endereco
                usuario['setor'] = setor
                break  # Sai do loop após encontrar e atualizar o usuário

    def excluir_usuario(self, user_id):
        # Cria uma nova lista de usuários excluindo aquele com o ID especificado
        self.usuarios = [usuario for usuario in self.usuarios if usuario['id'] != user_id]
