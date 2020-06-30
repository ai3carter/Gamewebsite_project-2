import pandas as pd
import os
import numpy as np
import psycopg2
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from sqlalchemy.sql import func
# We'll be using the database, Store our data in our database as opposed to in the array
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#################################################
# Database Setup
#################################################
game_database_path = "postgres:postgres@localhost:5432/game_db"
engine = create_engine(f"postgresql://{game_database_path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table
p= Base.classes.primaryv1
g = Base.classes.genre
# gm=Base.classes.game_mode
t=Base.classes.theme
# f=Base.classes.franchise
# age_des=Base.classes.age_description
# age_rating=Base.classes.age_rating
# similar=Base.classes.similar_game
# art=Base.classes.artwork
gr=Base.classes.genre_rating
tr=Base.classes.theme_rating
sgr=Base.classes.similar_game_name_p

ns=Base.classes.new_simil
# gmr=Base.classes.gamemode_rating
# conn = engine.connect()
# instantiate the SQLAlchemy object
# db = SQLAlchemy(app)
session = Session(engine)
# Create our database model
# set up the table through db.Column, and pass in the data type (string or integer)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/similar_games")
def similar_game_data():
    results3 = session.query(ns.name, ns.count, ns.rating).\
        order_by(ns.rating.desc()).\
        filter(ns.rating != None).\
        limit(50).all()
    df = pd.DataFrame(results3, columns=['game','count_of_similar_game', 'rating'])

    game = df['game'].values.tolist()
    similar_count = df['count_of_similar_game'].values.tolist()
    rating = df['rating'].values.tolist()
    data2 = {'x': game,
        'y': similar_count,
        "type":"bar"
        }
    return jsonify(data2)   


@app.route("/theme_count")
def theme_counting_data():
    results2 = session.query(tr.slug, func.count(tr.slug)).\
        order_by(func.count(tr.slug).desc()).\
        group_by(tr.slug).\
        all()
    df = pd.DataFrame(results2, columns=['theme','count'])
    theme = df['theme'].values.tolist()
    count = df['count'].values.tolist()
    data = {
        "x": theme,
        "y": count,
        "type":"bar"
    }
    return jsonify(data)
    
@app.route("/genre_rating")
def genre_rating_data():
    results = session.query(gr.slug, gr.rating).\
        order_by(gr.rating.desc()).\
        filter(gr.rating != None).\
        limit(5000).all()
    df = pd.DataFrame(results, columns = ['Genre', 'rating'])
    series = df.groupby('Genre')['rating'].mean()
    new_df = pd.DataFrame(series.reset_index(name = "Average Rating"))
    genres = new_df["Genre"].values.tolist()
    average_rating = new_df["Average Rating"].values.tolist()
    data1= {
        "x": genres,
        "y": average_rating,
        "type":"bar"
    }
    return jsonify(data1)

if __name__ == '__main__':
    app.run(debug=True)