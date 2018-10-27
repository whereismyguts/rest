import falcon
import json
from jsonschema import validate


class WheatherService(object):

    def validate_request(req, resp, resource, params):
        raise falcon.HTTPBadRequest('Bad request', msg)

    def check_temp(self, tmp_list):

        prev_sign = None
        for tmp in tmp_list:
            if tmp['t_air'] == 0:
                return True

            sign = tmp['t_air'] > 0 - tmp['t_air'] < 0
            if prev_sign is not None:
                if sign != prev_sign:
                    return True
            prev_sign = sign
        return False

    def on_post(self, req, resp):
        body = req.stream.read()
        try:
            data = json.loads(body)
            result = self.check_temp(data['data'].values())
        except Exception:
            resp.status = falcon.HTTP_400
            return
        resp.status = falcon.HTTP_200
        resp.body = str(result)


app = falcon.API()
service = WheatherService()
app.add_route('/api', service)
