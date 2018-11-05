import json
from flask_restful import Api, Resource, request
from rego.models import Entity
from rego import db


def _process_data(d):
    return json.dumps(d)


class EntityAPI(Resource):
    def get(self, eid):
        data = Entity.query.filter_by(id=eid).first_or_404()['data']
        return _process_data(data)


class EntitiesAPI(Resource):
    def get(self):
        entities = []
        for e in Entity.query.all():
            entities.append(e.entity_id)
        return json.dumps(entities)

    def put(self):
        new_e = Entity(data=json.loads(request.form['data']))
        db.session.add(new_e)
        db.session.commit()
        return {new_e.id: _process_data(new_e.data)}


def init(app):
    myapi = Api(app)
    myapi.add_resource(EntitiesAPI, '/api/entities')
    myapi.add_resource(EntityAPI, '/api/entities/<eid>')
