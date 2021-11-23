from wsgiref.simple_server import make_server

import falcon
import json
import Adafruit_DHT

def get_things():
    sensor = 11
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        return {"temp": temperature, "humidity": humidity}


class ThingsResource:
    def on_get(self, req, resp):

        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.text = json.dumps(get_things())

app = falcon.App()

things = ThingsResource()

app.add_route('/monitor', things)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        httpd.serve_forever()
