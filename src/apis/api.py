from flask import Flask
from flask_restful import Api, Resource
from sqlalchemy import create_engine
from controllers import MenuController
import urllib
from db_operations import SQLServerOperations
from flask_sqlalchemy import SQLAlchemy, declarative_base
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=pc-sql01.database.windows.net;DATABASE=pc-sql01;UID=pc;PWD=richtable123*#")
conn_str = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
SQLAlchemy(app)

db_operations = SQLServerOperations()

api.add_resource(MenuController, '/api/menu', resource_class_args=(db_operations,))

if __name__ == '__main__':
    app.run(debug=True)