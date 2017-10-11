"""Spacex Latest Information"""

import requests
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
import json




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "abc"


@app.route('/', methods=['GET'])
def get_data():
    """Show the latest spacex info"""

    spacex_str_json = requests.get('https://api.spacexdata.com/v1/launches/latest').content
    spacex_json_list = json.loads(spacex_str_json)

    for launch in spacex_json_list:
      flight_number = str(launch["flight_number"])
      launch_year = str(launch["launch_year"])
      rocket_name = str(launch["rocket"]["rocket_name"])
    
    return render_template('/homepage.html',
                            flight_number = flight_number,
                            launch_year = launch_year,
                            rocket_name = rocket_name)



    


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension


    app.run(host="0.0.0.0")