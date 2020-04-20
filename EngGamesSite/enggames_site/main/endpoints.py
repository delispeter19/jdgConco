from flask import Blueprint, render_template

from enggames_site.models import Page, Delegation, Pillar, Tier, Event, MachSection, Exec, JeuxDG, SMedia

main = Blueprint('main', __name__)

@main.route('/')
def home():
    pages = Page.query.all()
    page = Page.query.filter_by(title='HOME').first()
    delegations = Delegation.query.all()
    return render_template('main/base.html', pages=pages, page=page, delegations=delegations)


@main.route('/about')
def about():
    pages = Page.query.all()
    page = Page.query.filter_by(title='ABOUT').first()
    delegations = Delegation.query.all()
    pillars = Pillar.query.all()
    return render_template('main/about.html', pages=pages, page=page, pillars=pillars, delegations=delegations)


@main.route('/sponsors')
def sponsors():
    pages = Page.query.all()
    page = Page.query.filter_by(title='SPONSORS').first()
    delegations = Delegation.query.all()
    tiers = Tier.query.all()
    return render_template('main/sponsors.html', pages=pages, page=page, tiers=tiers, delegations=delegations)


@main.route('/events')
def events():
    pages = Page.query.all()
    page = Page.query.filter_by(title='EVENTS').first()
    evnts = Event.query.order_by(Event.id.desc())
    delegations = Delegation.query.all()
    return render_template('main/events.html', pages=pages, page=page, events=evnts, delegations=delegations)


@main.route('/machine')
def machine():
    pages = Page.query.all()
    page = Page.query.filter_by(title='MACHINE').first()
    sections = MachSection.query.all()
    delegations = Delegation.query.all()
    return render_template('main/machine.html', pages=pages, page=page, sections=sections, delegations=delegations)


@main.route('/execs')
def execs():
    pages = Page.query.all()
    page = Page.query.filter_by(title='EXECS').first()
    xx = Exec.query.all()
    delegations = Delegation.query.all()
    return render_template('main/execs.html', pages=pages, page=page, execs=xx, delegations=delegations)


@main.route('/awards')
def awards():
    pages = Page.query.all()
    page = Page.query.filter_by(title='AWARDS').first()
    jdgs = JeuxDG.query.all()
    titles = ["Prize", "Description"]
    delegations = Delegation.query.all()
    return render_template('main/awards.html', pages=pages, page=page, jdgs=jdgs, titles=titles, delegations=delegations)


@main.route('/contactus')
def contactus():
    pages = Page.query.all()
    page = Page.query.filter_by(title="CONTACT US").first()
    socials = SMedia.query.all()
    delegations = Delegation.query.all()
    return render_template('main/contactus.html', pages=pages, page=page, socials=socials, delegations=delegations)
