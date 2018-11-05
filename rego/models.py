from flask_login import UserMixin
from sqlalchemy_utils import JSONType
from rego import db

org_admins = db.Table(
    'org_admins', 
    db.Column('user_id',
              db.Integer,
              db.ForeignKey('user.id'),
              primary_key=True
    ),
    db.Column('organization_id',
              db.Integer,
              db.ForeignKey('organization.id'),
              primary_key=True
    )
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password_hash = db.Column(db.String)
    email = db.Column(db.String(254))
    role_id = db.Column(
        db.Integer, db.ForeignKey('role.id'), nullable=True
    )
                              
    role = db.relationship(
        'Role',
        backref=db.backref('roles', lazy=True)
    )

    organizations = db.relationship(
        'Organization',
        secondary=org_admins,
        lazy='subquery',
        backref=db.backref('users', lazy=True)
    )
    
class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
   
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254))
    contact_type_id = db.Column(
        db.Integer, db.ForeignKey('contact_type.id'), nullable=False
    )
                              
    contact_type = db.relationship(
        'ContactType',
        backref=db.backref('contacts', lazy=True)
    )

class ContactType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.String, unique=True)
    data = db.Column(JSONType)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           server_onupdate=db.func.now())
