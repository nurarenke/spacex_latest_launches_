"""Spacex Latest Information"""

import requests

from flask import Flask, render_template, request, flash, redirect, session




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "abc"


@app.route('/', methods=['GET'])
def get_data():
    """Show the latest spacex info"""

    spacex_json = requests.get('https://api.spacexdata.com/v1/launches/latest').content

    for spacex_dict in space_json:
        for title, info in spacex_dict:
            

    
    return 

    


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension


    app.run(host="0.0.0.0")