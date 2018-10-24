from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, URL

class OrganizationForm(FlaskForm):
    org_name = StringField('Organization name', validators=[DataRequired()]) 
    org_legalcontact_name = StringField('Legal contact name', validators=[DataRequired()]) 
    org_legalcontact_email = StringField('Legal contact email', validators=[DataRequired(), Email()])
    org_techadmin_name = StringField('Technical administrator name', validators=[DataRequired()]) 
    org_techadmin_email = StringField('Technical administrator email', validators=[DataRequired(), Email()]) 
   
class EntityForm(FlaskForm):
    entity_id = StringField('Entity ID', validators=[DataRequired(), URL()]) 
    entity_jwks = TextAreaField('Entity public key', validators=[DataRequired()])
    entity_statement = TextAreaField('Entity statement', validators=[DataRequired()])


