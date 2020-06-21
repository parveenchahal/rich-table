from flask import Flask
from flask_restful import Api, Resource

from sqlalchemy import create_engine
import urllib
from db import db
from operations import Operations, MenuOperations, FoodTypeOperations, MenuCategoryOperations
from controllers import Controller, MenuController, FoodTypeController, MenuCategoryController
from db_operations import SqlServerOperations

app = Flask(__name__)
api = Api(app)

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=pc-sql01.database.windows.net;DATABASE=pc-sql01;UID=pc;PWD=richtable123*#")
conn_str = "mssql+pyodbc:///?odbc_connect=%s" % params

app.config["SQLALCHEMY_DATABASE_URI"] = conn_str
db.init_app(app)

engine = db.get_engine(app)

db_operations = SqlServerOperations(engine)

menu_operations = MenuOperations(db_operations)
api.add_resource(MenuController, '/api/menu', resource_class_args=(menu_operations,))

food_type_operations = FoodTypeOperations(db_operations)
api.add_resource(FoodTypeController, '/api/food_type', resource_class_args=(food_type_operations,))

menu_category_operations = MenuCategoryOperations(db_operations)
api.add_resource(MenuCategoryController, '/api/menu_category', resource_class_args=(menu_category_operations,))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)