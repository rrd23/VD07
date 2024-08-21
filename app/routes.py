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
