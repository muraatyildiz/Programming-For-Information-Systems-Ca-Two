from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from flask_cors import CORS
import json
from sshtunnel import SSHTunnelForwarder
import mysql.connector
from dbconn import mysql
from flask import Blueprint
from product import product_api
from fileUpload import fileUpload_api



app = Flask(__name__)

# app.register_blueprint()
# app.register_blueprint(fileUpload_api)
app.register_blueprint(product_api, url_prefix='/product/')
app.register_blueprint(fileUpload_api, url_prefix='/file/')
CORS(app)



if __name__ == "__main__":
  #
   app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  #app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080