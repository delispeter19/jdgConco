from enggames_site import db, login_manager
from flask import current_app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


# define get user function for the login manager
@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    imgFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    events = db.relationship('Event', backref='author', lazy=True)

    def get_reset_token(self, expires_in=600):
        ser = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return ser.dumps({'admin_id': self.id}).decode('utf-8')

    @staticmethod
    def check_reset_token(token):
        ser = Serializer(current_app.config['SECRET_KEY'])
        try:
            admin_id = ser.loads(token)['admin_id']
        except:
            return None
        return Admin.query.get(admin_id)

    def __repr__(self):
        return f"Admin('{self.username}', '{self.email}', '{self.imgFile}')"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default='0000-00-00')
    fb_link = db.Column(db.String, nullable=False)
    imgFile = db.Column(db.String(20), nullable=False, default='powerHour.png')
    description = db.Column(db.Text, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

    def __repr__(self):
        return f"Event('{self.title}', '{self.last_updated}')"


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(200))
    name = db.Column(db.String)
    endpoint = db.Column(db.String)


class JeuxDG(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    year = db.Column(db.Integer)
    imgPath = db.Column(db.String)
    alt = db.Column(db.String)
    bgClr = db.Column(db.String)
    borderClr = db.Column(db.String)
    awards = db.relationship('Award', backref='jdg')


class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    position = db.Column(db.Integer)
    description = db.Column(db.String(100))
    jdg_id = db.Column(db.Integer, db.ForeignKey('jeuxDG.id'))


class MachSection(db.Model):
    __tablename__ = 'mach_section'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String)
    images = db.relationship('MachImages', backref='section')
    text = db.relationship('MachText', backref='section')


class MachImages(db.Model):
    __tablename__ = 'mach_images'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    imgPath = db.Column(db.String)
    alt = db.Column(db.String)
    current = db.Column(db.String)
    section_id = db.Column(db.Integer, db.ForeignKey('mach_section.id'))


class MachText(db.Model):
    __tablename__ = 'mach_text'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    sentence = db.Column(db.String)
    section_id = db.Column(db.Integer, db.ForeignKey('mach_section.id'))


class Pillar(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    imgPath = db.Column(db.String)
    description = db.Column(db.String)


class Exec(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    position = db.Column(db.String)
    email = db.Column(db.String)
    imgPath = db.Column(db.String)


class SMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    alt = db.Column(db.String)
    imgPath = db.Column(db.String)
    link = db.Column(db.String)


class Tier(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.Integer)
    sponsors = db.relationship('Sponsor', backref='tier')


class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    alt = db.Column(db.String)
    imgPath = db.Column(db.String)
    link = db.Column(db.String)
    tier_id = db.Column(db.Integer, db.ForeignKey('tier.id'))


class Delegation(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    alt = db.Column(db.String)
    imgPath = db.Column(db.String)
    link = db.Column(db.String)
