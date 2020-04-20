from flask import Blueprint, url_for, redirect, request, flash, render_template
from flask_login import current_user, login_user, logout_user

from enggames_site import db, bcrypt
from enggames_site.admins.forms import LoginForm, RequestResetForm, ResetPasswordForm
from enggames_site.admins.utils import reset_password_email, hashpassword
from enggames_site.models import Admin, Page, Delegation


admins = Blueprint('admins', __name__)


@admins.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin, remember=form.remember.data)
            next_pg = request.args.get('next')

            return redirect(next_pg) if next_pg else redirect(url_for('main.home'))
        else:
            flash('Login failed!', category='danger')
    pages = Page.query.all()
    page = Page.query.filter_by(title="EXEC LOGIN").first()
    delegations = Delegation.query.all()
    return render_template('login.html', pages=pages, page=page, form=form, delegations=delegations)


@admins.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@admins.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        reset_password_email(admin)
        flash('Check your email for the reset token.', category='primary')
        return redirect(url_for('admins.login'))
    pages = Page.query.all()
    page = Page.query.filter_by(title="EXEC LOGIN").first()
    delegations = Delegation.query.all()
    return render_template('reset_request.html', pages=pages, page=page, form=form, delegations=delegations)


@admins.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    admin = Admin.check_reset_token(token)

    if admin is None:
        flash('Token is invalid or has expired!', category='warning')
        return redirect(url_for('admins.reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        admin.password = hashpassword(form.password.data)
        db.session.commit()
        flash('Your password has been reset!', category='success')
        return redirect(url_for('admins.login'))

    pages = Page.query.all()
    page = Page.query.filter_by(title="EXEC LOGIN").first()
    delegations = Delegation.query.all()
    return render_template('reset_token.html', pages=pages, page=page, form=form, token=token, delegations=delegations)

