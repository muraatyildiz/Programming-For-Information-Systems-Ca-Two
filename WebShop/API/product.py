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

product_api = Blueprint('product_api', __name__)

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
product = Flask(__name__)
CORS(product)


@product_api.route("/test")#URL leading to method
def test(): # Name of the method
 return("Hello World!<BR/>THIS IS ANOTHER TEST!") 

@product_api.route("/yest")#URL leading to method
def yest(): # Name of the method
 return("Hello World!<BR/>THIS IS YET ANOTHER TEST!") 

@product_api.route("/add", methods=['GET', 'POST']) #Add product
def add():
  if request.method == 'POST':
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    stock = request.form['stock']
    imgUrl = request.form['imgUrl']
    description = request.form['description'] 
    cur = mysql.cursor() #create a connection to the SQL instance
    s='''INSERT INTO Product (Name, Category,Price,Stock,ImgURL,Description) VALUES('{}','{}','{}','{}','{}','{}');'''.format(name,category,price,stock,imgUrl,description)
    print(s)
    product.logger.info(s)
    cur.execute(s)
    mysql.commit()
  else:
    return render_template('add.html')

  return '{"Result":"Success"}'
@product_api.route("/update", methods=['GET', 'POST']) #Add product
def update():
  if request.method == 'POST':   
    id = request.form['id']
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    stock = request.form['stock']
    imgUrl = request.form['imgUrl']
    description = request.form['description']
    cur = mysql.cursor() #create a connection to the SQL instance
    s='''UPDATE Product SET Name ='{}' , Category='{}',Price='{}',Stock='{}',ImgURL='{}',Description='{}'  WHERE Product_ID ='{}';'''.format(name,category,price,stock,imgUrl,description,id)
    print(s)
    product.logger.info(s)
    cur.execute(s)
    mysql.commit()
  else:
    return render_template('add.html')
  return '{"Result":"Success"}'
@product_api.route("/list") #Default - Show Data
def hello(): # Name of the method
  cur = mysql.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM Product''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['id']=row[0]
    Result['name']=row[1]
    Result['category']=row[2]
    Result['stock']=row[3]
    Result['price']=row[4]
    Result['imgUrl']=row[5]
    Result['description']=row[6]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=product.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
@product_api.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_items(item_id):
 try:
        cur = mysql.cursor()
        cur.execute('DELETE FROM Product WHERE Product_ID = %s', (item_id,))
        mysql.commit()
        cur.close()       
        
        response = {
            'error' : False,
            'message': 'Product Deleted Successfully',
            'data': { 'item_id': item_id }
        }
        ret=product.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
           )
        return ret
 except Exception as e:
        # Handle any exceptions that may occur during the process
        response = {
            'error' : False,
            'message': f'Error Occurred: {e}',
            'data': None         
        }
        ret=product.response_class(
        response=json.dumps(response),
        status=500,
        mimetype='application/json'
           )
        return ret