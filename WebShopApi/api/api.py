from flask import Flask,render_template, redirect, request, jsonify, current_app, g
from flask_cors import CORS, cross_origin
from dbconn import ApiSQLEngine
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import text
from flask_restful import Resource, Api, abort,reqparse
import json
app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})

with app.app_context():
    # your code that needs the application context here
 
      # create product Model
      class Product(ApiSQLEngine.Model):
            
            id = ApiSQLEngine.Column(ApiSQLEngine.Integer, primary_key=True)
            name = ApiSQLEngine.Column(ApiSQLEngine.String(200), unique=True)
            price = ApiSQLEngine.Column(ApiSQLEngine.Float)
            description = ApiSQLEngine.Column(ApiSQLEngine.String(300))
         
            def __init__(self, name, price, description):
                  self.id = id
                  self.name = name
                  self.price = price
                  self.description = description
 
            def __repr__(self):
                  return f"Product(name={self.name}, description={self.description}, price={self.price})"

      # Define a Flask route for serving an HTML page
      @app.route('/')
      def index():
            productList = []
            conn = ApiSQLEngine.connect()
            result = conn.execute(text("SELECT * FROM dbo.ProductApiTable"))
            for row in result.fetchall():
                productList.append({"id": row[0], "name": row[1], "price": row[2], "description": row[3]})
        
            return render_template('index.html', productList = productList)
      
      class Square(Resource):
  
        def get(self, num):
  
            return jsonify({'square': num**2})

      # Create Flask-RESTful resource to interact with your database
      @app.route('/products')

      def productindex():
            productList = []
            conn = ApiSQLEngine.connect()
            result = conn.execute(text("SELECT * FROM dbo.ProductApiTable"))
            for row in result.fetchall():
                productList.append({"id": row[0], "name": row[1], "price": row[2], "description": row[3]})
        
            return render_template('index.html', productList = productList)
       
      class ProductResource(Resource):
           
           # Get a product by ID
          def get(self):
                conn = ApiSQLEngine.connect()
                result = conn.execute(text("SELECT * FROM dbo.ProductApiTable"))
               
                return jsonify(result)
# Add the resource to the API
api = Api(app)
api.add_resource(ProductResource, '/products')      
api.add_resource(Square, '/square/<int:num>')          
 
# product Schema
class appSchema(ApiMa.Schema):
    class Meta:
        fields    = ('id', 'name', 'price', 'description')

# Initialize Schema
product_schema    = appSchema()
app_schema        = appSchema(many=True)

# Creation of the database tables within the application context.

if __name__ == "__main__":
    with app.app_context():
      ApiSQLEngine.create_all()
      app.run(debug=True)