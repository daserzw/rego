from wtforms.validators import ValidationError
import json

class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'This element already exists.'
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class JsonString(object):
    def __init__(self, message=None):
        if not message:
            message = u'This field must be a valid JSON string.'
        self.message = message
    
    def __call__(self, form, field):
        try:
            json.loads(field.data)
        except:
            raise ValidationError(self.message) 


