from flask_restful import Resource, fields, marshal_with
from app.models import Host


host_fields = {
    'id': fields.Integer,
    'hostname': fields.String,
    'll_ip': fields.String,
    'ctrl_if': fields.String,
    'last_seen': fields.DateTime
}


class HostResource(Resource):
    @marshal_with(host_fields)
    def get(self):
        return Host.query.all()
