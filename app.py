from flask import Flask, jsonify, render_template
import sqlalchemy
import flask_sqlalchemy
import pandas
import os

print (os.environ)
# if not os.environ.get('Dyno'):
#     import config
#     print(config.name)
    
# if os.environ.get("JAWSDB_URL"):
#     dburl=os.environ["JAWSDB_URL"]
# else:
#     dburl = config.dburl

# engine= sqlalchemy.create_engine(dburl)

# df= pandas.read_sql("Select * From GDP_Brazil", engine)
# print(df)
# app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(df.to_json(orient= "records"))

if __name__=="__main__":
    app.run