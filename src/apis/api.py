from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from controllers import MenuController
import urllib
from db_operations import SQLServerOperations

app = Flask(__name__)
api = Api(app)

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=pc-sql01.database.windows.net;DATABASE=pc-sql01;UID=pc;PWD=richtable123*#")
conn_str = "mssql+pyodbc:///?odbc_connect=%s" % params
sql_engine = create_engine(conn_str, echo=True)
db_operations = SQLServerOperations(sql_engine)
api.add_resource(MenuController, '/api/menu', resource_class_args=(db_operations,))

if __name__ == '__main__':
    app.run(debug=True)