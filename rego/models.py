from flask_login import UserMixin
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
        db.Integer, db.ForeignKey('contact_type.id'), nullable=False
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
    data = db.Column(db.JSON)
    
    @property
    def entity_id(self):
        return self.data['sub']    

