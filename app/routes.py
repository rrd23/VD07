from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import EditProfileForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        flash(f'Profile updated for {form.username.data}!', 'success')
        return redirect(url_for('main.edit_profile'))
    return render_template('edit_profile.html', title='Edit Profile', form=form)

