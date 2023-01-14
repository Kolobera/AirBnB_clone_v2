#!/usr/bin/python3
"""Displays hbnbfilters"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters_hbnb():
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()
