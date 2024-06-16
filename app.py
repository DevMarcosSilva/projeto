from flask import Flask
from routes import setup_routes  # Importa a função setup_routes do módulo routes

class FlaskApp:
    def __init__(self):
        # Inicializa a aplicação Flask
        self.app = Flask(__name__)
        # Configura as rotas da aplicação
        self.setup_routes()

    def setup_routes(self):
        # Chama a função setup_routes passando a aplicação Flask para configurar as rotas
        setup_routes(self.app)

    def run(self):
        # Executa a aplicação Flask em modo debug
        self.app.run(debug=True)

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Cria uma instância da classe FlaskApp
    flask_app = FlaskApp()
    # Executa a aplicação Flask
    flask_app.run()
