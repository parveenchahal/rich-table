from flask import Flask
from flask_restful import Api, Resource

from sqlalchemy import create_engine
import urllib

from operations import MenuOperations
from controllers import MenuController
from db_operations import SqlServerOperations

app = Flask(__name__)
api = Api(app)

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=pc-sql01.database.windows.net;DATABASE=pc-sql01;UID=pc;PWD=richtable123*#")
conn_str = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine(conn_str)
db_operations = SqlServerOperations(engine)

menu_operations = MenuOperations(db_operations)
api.add_resource(MenuController, '/api/menu', resource_class_args=(menu_operations,))

if __name__ == '__main__':
    app.run(debug=True)