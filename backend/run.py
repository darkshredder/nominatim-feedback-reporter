
import falcon
from wsgiref import simple_server

from middlewares.json_validator import RequireJSON
from routes import routes as _routes


# initialize the falcon application

middlewares = [RequireJSON()]

app = application = falcon.App(middleware=middlewares)


# Initialize all api routes.
for apiRoute, apiClass in _routes.items():
	app.add_route(apiRoute, apiClass)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()