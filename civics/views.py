from flask import request, jsonify

from . import app
from .models import Story, District, Representative


@app.route('/')
def index():
    return "Hello World"


@app.route('/stories', methods=['GET'])
def get_stories():
    stories = Story.select()
    story_list = [x.json() for x in stories]
    return jsonify({'stories': story_list})


@app.route('/districts', methods=['GET'])
def get_districts():
    districts = District.select()
    district_list = [x.json() for x in districts]
    return jsonify({'districts': district_list})


@app.route('/representatives', methods=['GET'])
def get_representatives():
    representatives = Representative.select()
    representative_list = [x.json() for x in representatives]
    return jsonify({'representatives': representative_list})
