import json
from bson import ObjectId

response_not_found = 404
response_invalid = 403
response_ok = 200


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
