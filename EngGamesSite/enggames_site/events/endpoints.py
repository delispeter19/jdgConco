import os
import secrets
from datetime import datetime

from flask import Blueprint, flash, url_for, render_template, request, redirect, current_app
from flask_login import login_required, current_user

from enggames_site import db
from enggames_site.events.forms import EventForm
from enggames_site.models import Event, Page, Delegation

events = Blueprint('events', __name__)

@events.route('/events/add', methods=['GET', 'POST'])
@login_required
def add_new_event():
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(title=form.title.data,
                          date=form.date.data,
                          fb_link=form.fb_link.data,
                          description=form.description.data,
                          author=current_user)
        if form.imgFile.data:
            rand = secrets.token_hex(8)
            _, ext = os.path.splitext(form.imgFile.data.filename)
            img = rand + ext
            img_path = os.path.join(current_app.root_path, 'static/assets/events', img)
            form.imgFile.data.save(img_path)
            new_event.imgFile = img
        db.session.add(new_event)
        db.session.commit()
        flash('Event Added', category='success')
        return redirect(url_for('main.events'))
    pages = Page.query.all()
    page = Page.query.filter_by(title='EVENTS').first()
    delegations = Delegation.query.all()
    return render_template('add_event.html', pages=pages, page=page, form=form, delegations=delegations)


@events.route('/events/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    form = EventForm()
    event = Event.query.get(id)
    if form.validate_on_submit():
        event.title = form.title.data
        if form.imgFile.data:
            rand = secrets.token_hex(8)
            _, ext = os.path.splitext(form.imgFile.data.filename)
            img = rand + ext
            img_path = os.path.join(current_app.root_path, 'static/assets/events', img)
            form.imgFile.data.save(img_path)
            event.imgFile = img
        event.date = form.date.data
        event.fb_link = form.fb_link.data
        event.description = form.description.data
        event.last_updated = datetime.utcnow()
        event.author = current_user
        db.session.commit()
        flash('Event Modified', category='success')
        return redirect(url_for('main.events'))
    elif request.method == 'GET':
        form.title.data = event.title
        form.date.data = event.date
        form.fb_link.data = event.fb_link
        form.imgFile.data = event.imgFile
        form.description.data = event.description
    pages = Page.query.all()
    page = Page.query.filter_by(title='EVENTS').first()
    delegations = Delegation.query.all()
    return render_template('edit_event.html', pages=pages, page=page, form=form, event=event, delegations=delegations)


@events.route('/event/delete/<id>', methods=['POST'])
@login_required
def delete_event(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    flash('Event Deleted', category='danger')
    return redirect(url_for('main.events'))