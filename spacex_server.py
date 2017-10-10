"""Spacex Latest Information"""

import requests
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "abc"


@app.route('/', methods=['GET'])
def get_data():
    """Show the latest spacex info"""

    spacex_json = requests.get('https://api.spacexdata.com/v1/launches/latest').content

    display_info = clean_json(spacex_json)
    
    return render_template('/homepage.html',
                            display_info=display_info)
#############################################################################
#Helper functions
def clean_json(json_dict):
    '''iterates through json dictionary objects and print everything'''

    for title, info in json_dict.iteritems():
        if isinstance(info, dict):
            clean_json(info)
        else:
            print "{0} : {1}".format(title, info)


    


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension


    app.run(host="0.0.0.0")