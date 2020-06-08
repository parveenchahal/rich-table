import copy
from flask import jsonify
from db import db
from models.abstract_model import Model

DbModel = db.Model

setattr(DbModel, 'to_dict', getattr(Model, 'to_dict'))
setattr(DbModel, 'to_dict_list', getattr(Model, 'to_dict_list'))
