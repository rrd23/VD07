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
