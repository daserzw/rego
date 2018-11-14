import json
from sqlalchemy.exc import IntegrityError
from flask import Blueprint
from flask_restful import Api, Resource, request
from rego.models import Entity
from rego import db
from urllib.parse import quote_plus, unquote_plus


class EntityAPI(Resource):
    def get(self, eid):
        if eid.isdigit():
            q = Entity.query.filter_by(id=eid).first_or_404()
        else:
            eid_parsed = unquote_plus(eid)
            q = Entity.query.filter_by(entity_id=eid_parsed).first_or_404()
        return q.data

    def delete(self, eid):
        if eid.isdigit():
            q = Entity.query.filter_by(id=eid).first_or_404()
        else:
            eid_parsed = unquote_plus(eid)
            q = Entity.query.filter_by(entity_id=eid_parsed).first_or_404()
        db.session.delete(q)
        db.session.commit()
        return '', 204


class EntitiesAPI(Resource):
    def get(self):
        entities = dict()
        for e in Entity.query.all():
            entities[e.id] = {"entityID": e.entity_id,
                              "url": "{}api/entities/{}".format(request.url_root, quote_plus(e.entity_id)) }
        return entities

    def put(self):
        data = json.loads(request.form['data'])
        new_e = Entity(data=data)
        # FIXME: a complete parser is needed!
        try:
            new_e.entity_id = data['sub']
        except KeyError:
            return {"message": "The uploaded JSON data doesn't contain a 'sub'"}, 422
        try:
            new_e.org_id = int(request.form['org'])
        except KeyError:
            new_e.org_id = db.null()

        db.session.add(new_e)
        try:
            db.session.commit()
            return {new_e.id: new_e.data}
        except IntegrityError:
            return {"message": "The uploaded JSON contains an existing 'sub'"}, 422


def init(app):
    myapi = Api(app)
    myapi.add_resource(EntityAPI, '/api/entities/<path:eid>')
    myapi.add_resource(EntitiesAPI, '/api/entities')
