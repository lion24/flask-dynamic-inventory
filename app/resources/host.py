from flask_restful import Resource


class Host(Resource):
    def get(self):
        return {'hello': 'world'}