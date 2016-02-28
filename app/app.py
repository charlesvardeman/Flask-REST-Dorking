
from rdflib import Graph, BNode, Literal, URIRef, Dataset
from rdflib.namespace import FOAF
from flask import Flask, make_response
import flask_rdf
from flask_rdf.flask import returns_rdf
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# set up a custom formatter to return turtle in text/plain to browsers
custom_formatter = flask_rdf.FormatSelector()
custom_formatter.wildcard_mimetype = 'application/ld+json'
custom_formatter.add_format('application/ld+json', 'json-ld')
custom_decorator = flask_rdf.flask.Decorator(custom_formatter)



ds = Dataset(default_union=True)

with open('./dectectorfinalstate.owl', "r") as f:
    result = ds.parse(f, format="application/rdf+xml")

class HelloWorld(Resource):
    @custom_decorator
    def get(self):
        return ds

api.add_resource(HelloWorld, '/detectorfinalstate')


@app.route("/")
def main():
    # This is cached, so for development it is better
    # to use make_response
    # return send_file('templates/index.html')'
    return make_response(open('templates/index.html').read())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
