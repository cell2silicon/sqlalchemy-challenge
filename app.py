import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create Engine
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
        f"Welcome to Climate Analysis for Hawaii!<br/>"
        f"Available Routes are:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def percipitation():
    
    percipitation = session.query(Measurement.date,Measurement.prcp).all()

    perc = {date: prcp for date, prcp in percipitation}
    return jsonify(perc)    


@app.route("/api/v1.0/stations")
def station():
    station = session.query(Station.name).all()
    return jsonify(station)


@app.route("/api/v1.0/tobs")
def tobs():
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= last_year).filter(Measurement.station == "USC00519281").all()
    return jsonify(tobs)


@app.route("/api/v1.0/temp/<start>")
def temp_start(start):
    temp = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    return jsonify(temp[0])


@app.route("/api/v1.0/temp/<start>/<end>")
def temp_end(start,end):
    temp = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(temp[0])

if __name__ == "__main__":
    app.run(debug=True)
