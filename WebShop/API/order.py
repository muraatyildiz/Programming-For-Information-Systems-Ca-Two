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

order_api = Blueprint('order_api', __name__)

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
order = Flask(__name__)
CORS(order)

@order_api.route("/add", methods=['GET', 'POST']) #Add order
def add():
  if request.method == 'POST':
    customerFullName = request.form['customerFullName']
    customerEmail = request.form['customerEmail']
    customerPhoneNumber = request.form['customerPhoneNumber']
    paymentDone = request.form['paymentDone']
    shippingName = request.form['shippingName']
    shippingAddress = request.form['shippingAddress']
    shippingPhoneNumber = request.form['shippingPhoneNumber']
    shippingDate = request.form['shippingDate']
    shippingCardMessage = request.form['shippingCardMessage']
    orderDate = request.form['orderDate'] 
    totalPrice = request.form['totalPrice']  
 
 
    cur = mysql.cursor() #create a connection to the SQL instance
    s='''INSERT INTO Orders(CustomerFullName, CustomerEmail,CustomerPhoneNumber,PaymentDone,ShippingName,
     ShippingAddress,ShippingPhoneNumber,ShippingDate,ShippingCardMessage,OrderDate,TotalPrice) 
     VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(customerFullName,customerEmail,customerPhoneNumber,
                                                      paymentDone,shippingName,shippingAddress,shippingPhoneNumber,
                                                      shippingDate,shippingCardMessage,orderDate,totalPrice)
   
    order.logger.info(s)
    cur.execute(s)
    mysql.commit()
    orderId=cur.lastrowid
    i = 0
    while f'products[{i}][id]' in request.form:
     productId=int(request.form[f'products[{i}][id]'])
     productName=request.form[f'products[{i}][name]']
     totalProductPrice =int(request.form[f'products[{i}][quantity]'])*int(request.form[f'products[{i}][price]']) 
     quantity = int(request.form[f'products[{i}][quantity]'])
     a='''INSERT INTO Ordered_Product (Product_ID, Order_Number,ProductName,TotalPrice,Quantity) 
     VALUES('{}','{}','{}','{}','{}');'''.format(productId,orderId,productName,totalProductPrice,quantity) 
     order.logger.info(a)
     cur.execute(a)     
     mysql.commit()   
     i+=1
  else:
    return render_template('add.html')

  return '{"Result":"Success"}'
@order_api.route("/list") #Default - Show Data
def hello(): # Name of the method
  cur = mysql.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT Ordered_Product.Ordered_Product_ID, Orders.Order_Number, Orders.CustomerFullName, Ordered_Product.ProductName, Orders.OrderDate, Orders.ShippingDate, Orders.ShippingAddress
FROM Orders
INNER JOIN Ordered_Product
ON Orders.Order_Number=Ordered_Product.Order_Number''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['id']=row[0]
    Result['orderNumber']=row[1]
    Result['customerFullName']=row[2]
    Result['productName']=row[3]
    Result['orderDate']=row[4]
    Result['shippingDate']=row[5]
    Result['shippingAddress']=row[6]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=order.response_class(
    response=json.dumps(response,indent=4, sort_keys=True, default=str),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
