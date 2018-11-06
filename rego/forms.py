from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, URL
from .util.validators import Unique, JsonString
from .models import Entity, Organization


class RegisterEntityForm(FlaskForm):
    entity_id = StringField('Entity ID', validators=[DataRequired(), URL(),
        Unique(Entity, Entity.entity_id,message='There is already an entity with this entity ID.')]) 
    entity_jwks = TextAreaField('Entity public key', render_kw={"rows": 10, "cols": 70}, validators=[DataRequired(), JsonString()])
    entity_statement = TextAreaField('Entity statement', render_kw={"rows": 10, "cols": 70}, validators=[DataRequired(), JsonString()])


class RegisterOrganizationForm(FlaskForm):
    org_name = StringField('Organization name', validators=[DataRequired(),
        Unique(Organization, Organization.name,message='There is already an organization with this name.')])
    org_legalcontact_name = StringField('Legal contact name', validators=[DataRequired()]) 
    org_legalcontact_email = StringField('Legal contact email', validators=[DataRequired(), Email()])
    org_techadmin_name = StringField('Tech admin name', validators=[DataRequired()]) 
    org_techadmin_email = StringField('Tech admin email', validators=[DataRequired(), Email()]) 
   



