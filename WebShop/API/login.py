from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from flask_cors import CORS
import json
from sshtunnel import SSHTunnelForwarder
import mysql.connector
from dbconn import mysql
from logging.config import dictConfig
from flask import Blueprint

login_api = Blueprint('login_api', __name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
login = Flask(__name__)
CORS(login)

@login_api.route("/check", methods=['GET', 'POST']) #Add order
def add():
 
  userName = request.form['userName']
  password = request.form['password']
  cur = mysql.cursor()
  cur.execute('''SELECT * FROM Administrator''') 
  rv = cur.fetchall()
  Result={}
  for row in rv:
   if row[5] == userName and row[6] == password:
      Result['id']=row[0]
      Result['fullName']=row[1] +" "+ row[2]
      Result['phoneNumber']=row[3]
      Result['email']=row[4]
      Result['userName']=row[5]
      Result['role']=row[7] 
  if Result == {}:
   return '{"Result":"error"}'
  else:    
   response={'Results':Result}
   ret=login.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret
@login_api.route("/list") 
def list(): 
  cur = mysql.cursor()
  cur.execute('''SELECT * FROM Administrator''') 
  rv = cur.fetchall()
  Results=[]
  for row in rv:
    Result={}
    Result['id']=row[0]
    Result['fullName']=row[1] +" "+ row[2]
    Result['phoneNumber']=row[3]
    Result['email']=row[4]
    Result['userName']=row[5]
    Result['role']=row[7]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=login.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret 