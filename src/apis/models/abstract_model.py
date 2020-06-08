from sqlalchemy.orm.state import InstanceState
import copy
from json import JSONEncoder 
from dataclasses import fields
from flask import jsonify

class Model(object):

    @staticmethod
    def to_obj(dict, model_class_ref):
        return model_class_ref(**dict)

    @staticmethod
    def to_obj_list(list_of_dict, model_class_ref):
        return ([model_class_ref.to_obj(item) for item in list_of_dict])
    
    def to_dict(self):
        d = copy.deepcopy(self.__dict__)
        try:
            if(isinstance(d['_sa_instance_state'], InstanceState)):
                del d['_sa_instance_state']
        except:
            pass
        return d

    @staticmethod
    def to_dict_list(model_obj_list):
        return ([model_obj.to_dict() for model_obj in model_obj_list])

    def validate_type(self):
        for field in fields(self):
            attr = getattr(self, field.name)
            if attr is not None and not isinstance(attr, field.type):
                error_msg = "Expected type of {0.name} is {1}, given {0.type}".format(field, type(attr))
                raise ValueError(error_msg)

    def __post_init__(self):
        self.validate_type()