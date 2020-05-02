from datetime import datetime

from flask import Blueprint, request, jsonify

from enggames_site import db
from enggames_site.models import Admin, Page, Event
from enggames_site.restApi.utils import hashpassword
from enggames_site.schemas import admin_schema, admins_schema, page_schema, pages_schema, event_schema, events_schema

api = Blueprint('api', __name__)


# ======== REST-ful API =============================


@api.route('/api/admin', methods=['POST'])
def add_admin():
    username = request.json['username']
    email = request.json['email']
    imgFile = request.json['imgFile']
    password = hashpassword(request.json['password'])
    new_admin = Admin(username=username, email=email, password=password, imgFile=imgFile)
    db.session.add(new_admin)
    db.session.commit()
    return admin_schema.dump(new_admin)


@api.route('/api/admin', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    result = admins_schema.dump(admins)
    # this is an array and not a dict or Response inst.
    return jsonify(result)


@api.route('/api/admin/<id>', methods=['GET'])
def get_admin(id):
    admin = Admin.query.get(id)
    return admin_schema.dump(admin)


@api.route('/api/admin/<id>', methods=['PUT'])
def update_admin(id):
    admin = Admin.query.get(id)
    admin.username = request.json['username'] if 'username' in request.json else admin.username
    admin.email = request.json['email'] if 'email' in request.json else admin.email
    admin.imgFile = request.json['imgFile'] if 'imgFile' in request.json else admin.imgFile
    admin.password = hashpassword(request.json['password']) if 'password' in request.json else admin.password
    db.session.commit()
    return admin_schema.jsonify(admin)


@api.route('/api/admin/<id>', methods=['DELETE'])
def del_admin(id):
    admin = Admin.query.get(id)
    db.session.delete(admin)
    db.session.commit()
    return admin_schema.jsonify(admin)


@api.route('/api/page', methods=['POST'])
def add_page():
    title = request.json['title']
    name = request.json['name']
    description = request.json['description']
    endpoint = request.json['endpoint']
    new_page = Page(title=title, name=name, description=description, endpoint=endpoint)
    db.session.add(new_page)
    db.session.commit()
    return page_schema.dump(new_page)


@api.route('/api/page', methods=['GET'])
def get_pages():
    pages = Page.query.all()
    result = pages_schema.dump(pages)
    # this is an array and not a dict or Response inst.
    return jsonify(result)


@api.route('/api/page/<id>', methods=['GET'])
def get_page(id):
    page = Page.query.get(id)
    return page_schema.dump(page)


@api.route('/api/page/<id>', methods=['PUT'])
def update_page(id):
    page = Page.query.get(id)
    page.title = request.json['title']
    page.name = request.json['name']
    page.description = request.json['description']
    page.endpoint = request.json['endpoint']
    db.session.commit()
    return page_schema.jsonify(page)


@api.route('/api/page/<id>', methods=['DELETE'])
def del_page(id):
    page = Page.query.get(id)
    db.session.delete(page)
    db.session.commit()
    return page_schema.jsonify(page)


@api.route('/api/event', methods=['POST'])
def add_event():
    title = request.json['title']
    date = request.json['date']
    fb_link = request.json['fb_link']
    imgFile = request.json['imgFile']
    description = request.json['description']
    admin_id = request.json['admin_id']
    new_event = Event(title=title, date=date, fb_link=fb_link, imgFile=imgFile, description=description, admin_id=admin_id)
    db.session.add(new_event)
    db.session.commit()
    return event_schema.dump(new_event)


@api.route('/api/event', methods=['GET'])
def get_events():
    events = Event.query.all()
    result = events_schema.dump(events)
    # this is an array and not a dict or Response inst.
    return jsonify(result)


@api.route('/api/event/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.get(id)
    return event_schema.dump(event)


@api.route('/api/event/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.get(id)
    event.title = request.json['title']
    event.date = request.json['date']
    event.fb_link = request.json['fb_link']
    event.imgFile = request.json['imgFile']
    event.description = request.json['description']
    event.last_updated = datetime.utcnow()
    event.admin_id = request.json['admin_id']
    db.session.commit()
    return event_schema.dump(event)


@api.route('/api/event/<id>', methods=['DELETE'])
def del_event(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return event_schema.dump(event)

# ============================================================
