from flask import abort, jsonify, request

from . import app
from .models import Story, District, Representative
from .utils import validate_story


@app.route('/')
def index():
    return "Hello World"


@app.route('/stories', methods=['GET'])
def get_stories():
    stories = Story.select()
    story_list = [x.json() for x in stories]
    return jsonify({'stories': story_list})


@app.route('/stories', methods=['POST'])
def submit_story():
    form = request.form
    if not validate_story(form):
        return abort(400)
    story = Story(name=form['name'],
                  story=form['story'],
                  district=form['district'],
                  date=form['date'])
    story.save()
    return jsonify(story.json())


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
