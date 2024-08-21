from flask import Flask


def create_app():
    # Создаем экземпляр приложения Flask
    app = Flask(__name__)

    # Устанавливаем секретный ключ для защиты форм и сессий
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Импортируем и регистрируем основной блюпринт с маршрутами
    from app.routes import main
    app.register_blueprint(main)

    # Возвращаем экземпляр приложения
    return app
