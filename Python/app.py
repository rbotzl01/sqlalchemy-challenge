# import Flask
from flask import Flask, jsonify

# Create an app, being sure to pass __name__
app = Flask(__name__)


# Define what to do when a user hits the index route
@app.route("/api/v1.0/stations")
def precipitation():
    """Return the Precipitation Data data as json"""

    return jsonify(precip_df)


# Define what to do when a user hits the /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    """Return the Station Data data as json"""

    return jsonify(stations_df)
