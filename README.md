# Flask Profile Edit Application

This is a simple Flask application that allows users to edit their profile information, including username, email, and password. The application is designed using Flask-WTF for form handling and includes basic validation for the input fields.

## Project Structure


Я перепишу проект с подробными комментариями в каждом файле и создам README.md файл, который поможет другим разработчикам понять и запустить проект.

Структура проекта
arduino
Копировать код
/project_folder
│
├── run.py
└── app/
    ├── __init__.py
    ├── forms.py
    ├── routes.py
    ├── templates/
    │   ├── home.html
    │   └── edit_profile.html
    └── static/
        ├── css/
        └── js/
└── README.md
1. app/__init__.py
python
Копировать код
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
2. app/routes.py
python
Копировать код
from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import EditProfileForm

# Создаем объект Blueprint, который будет содержать все маршруты
main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Этот маршрут отображает главную страницу
    return render_template('home.html')

@main.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    # Создаем экземпляр формы для редактирования профиля
    form = EditProfileForm()
    
    # Проверяем, была ли форма отправлена и корректно ли она заполнена
    if form.validate_on_submit():
        # Если форма валидна, выводим сообщение об успешном обновлении профиля
        flash(f'Profile updated for {form.username.data}!', 'success')
        
        # Перенаправляем пользователя обратно на страницу редактирования профиля
        return redirect(url_for('main.edit_profile'))
    
    # Если форма не отправлена или некорректна, отображаем страницу с формой
    return render_template('edit_profile.html', title='Edit Profile', form=form)
3. app/forms.py
python
Копировать код
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class EditProfileForm(FlaskForm):
    # Поле для ввода имени пользователя с проверкой на обязательность и длину
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    
    # Поле для ввода электронной почты с проверкой на обязательность и правильный формат
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    # Поле для ввода пароля с проверкой на обязательность и минимальную длину
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message="Password should be at least 6 characters long")
    ])
    
    # Поле для подтверждения пароля с проверкой на соответствие введенному паролю
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    
    # Кнопка для отправки формы
    submit = SubmitField('Update Profile')
4. app/templates/home.html
html
Копировать код
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-4">Welcome to the Home Page</h1>
        <!-- Ссылка для перехода на страницу редактирования профиля -->
        <p><a href="{{ url_for('main.edit_profile') }}" class="btn btn-primary">Edit Profile</a></p>
    </div>
</body>
</html>
5. app/templates/edit_profile.html
html
Копировать код
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Profile</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h2 class="mt-4">Edit Profile</h2>
        <!-- Форма для редактирования профиля -->
        <form method="POST" action="{{ url_for('main.edit_profile') }}">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.username.label(class="form-label") }}
                {{ form.username(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.password.label(class="form-label") }}
                {{ form.password(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.confirm_password.label(class="form-label") }}
                {{ form.confirm_password(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
6. run.py
python
Копировать код
from app import create_app

# Создаем экземпляр приложения, используя фабричную функцию
app = create_app()

if __name__ == '__main__':
    # Запускаем приложение в режиме отладки
    app.run(debug=True)
7. README.md
Теперь создадим подробный README файл для проекта:

markdown
Копировать код
# Flask Profile Edit Application

This is a simple Flask application that allows users to edit their profile information, including username, email, and password. The application is designed using Flask-WTF for form handling and includes basic validation for the input fields.

## Project Structure

/project_folder
│
├── run.py # Entry point for running the application
└── app/
├── init.py # Initializes the Flask application and registers blueprints
├── forms.py # Contains the WTForms used for profile editing
├── routes.py # Contains the routes for the application
├── templates/ # Folder containing HTML templates
│ ├── home.html # Template for the home page
│ └── edit_profile.html # Template for the profile editing page
└── static/ # Folder for static files like CSS, JavaScript
├── css/
└── js/

## How to Run

1. **Clone the repository**:
    ```
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. **Navigate to the project directory**:
    ```
    cd project_folder
    ```

3. **Install the required packages**:
    ```
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```
    python run.py
    ```

5. **Open your browser** and go to `http://127.0.0.1:5000/` to see the application in action.

## Features

- **Home Page**: A simple landing page with a link to the profile edit page.
- **Profile Edit Form**: A form that allows users to update their username, email, and password with validation.
- **Form Validation**: Includes validation for required fields, email format, and password matching.

## Dependencies

- **Flask**: The web framework used for building the application.
- **Flask-WTF**: Extension for integrating WTForms with Flask.
- **WTForms**: A flexible form validation and rendering library for Python.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


