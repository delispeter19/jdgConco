from flask import Blueprint, render_template

from enggames_site.models import Page, Delegation

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(err):
    pages = Page.query.all()
    delegations = Delegation.query.all()
    return render_template('errors/404.html', pages=pages, delegations=delegations, err=err), 404


@errors.app_errorhandler(403)
def error_403(err):
    pages = Page.query.all()
    delegations = Delegation.query.all()
    return render_template('errors/403.html', pages=pages, delegations=delegations, err=err), 403


@errors.app_errorhandler(500)
def error_500(err):
    pages = Page.query.all()
    delegations = Delegation.query.all()
    return render_template('errors/500.html', pages=pages, delegations=delegations, err=err), 500

